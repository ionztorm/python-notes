"""Flight finder.

Accepts a list of destinations and finds the cheapest flights to each destination.
Updates Google Sheet with iata and country codes if not present.
"""

import datetime as dt

from amadeus import Amadeus
from mailer import Mailer
from sheety import Sheety


class FlightFinder:
    """Flight finder class."""

    def __init__(self) -> None:
        """Construct an instance of FlightFinder."""
        self.sheety = Sheety(project_name="flightDeals", sheet_name="prices")
        self.amadeus = Amadeus()
        self.mailer = Mailer()
        self.sheet_data = self.sheety.read()["prices"]
        self.sanitised_data = []

    def sanitise_data(self) -> None:
        """Run the flight search."""
        print("Sanitising data...")
        for destination in self.sheet_data:
            require_update = False
            city = destination["city"]
            country = destination["country"]
            iata_code = destination["iataCode"]
            country_code = destination["countryCode"]
            lowest_price = destination["lowestPrice"]
            id = destination["id"]

            print("--------------------------")
            print(f">>> Sanitising {city}, {country}")

            # if no country code, get country code
            if not country_code:
                require_update = True
                print(">>> No country code found -> Searching")
                country_code = self.amadeus.get_country_code(country=country)
                if country_code:
                    print(f"<<< Country code found: {country_code}")

            # if no iata code, get iata code
            if not iata_code:
                require_update = True
                print(">>> No IATA code found -> Searching")
                iata_code = self.amadeus.get_iata_code(city=city, country_code=country_code)
                if iata_code:
                    print(f"<<< IATA code found: {iata_code}")

            # update (PUT) sheet
            if require_update:
                new_data = {
                    "price": {
                        "iataCode": iata_code,
                        "countryCode": country_code,
                    }
                }
                print(">>> Updating sheet...")
                self.sheety.update(row=id, data=new_data)
                print("<<< Sheet updated.")

            self.sanitised_data.append(
                {
                    "city": city,
                    "country": country,
                    "country_code": country_code,
                    "iata_code": iata_code,
                    "lowest_price": lowest_price,
                    "id": id,
                }
            )

    def flight_search(self) -> None:
        """Run the flight search."""
        print("Searching for flights...")
        for destination in self.sanitised_data:
            city = destination["city"]
            country_code = destination["country_code"]
            lowest_price = destination["lowest_price"]
            iata_code = destination["iata_code"]

            print("--------------------------")
            print(
                f">>> Searching for flights to {city}, {country_code},"
                f" with a lowest price of {lowest_price}"
            )
            offers = self.amadeus.get_flights(
                origin="LPL",
                destination=iata_code,
                departure_date=(dt.datetime.now() + dt.timedelta(days=1)).strftime("%Y-%m-%d"),
                adults=1,
                max_offers=5,
                max_price=lowest_price,
                currency="GBP",
            )

            if len(offers):
                self.format_flight_deals(data=offers, from_code="LPL", to_code=iata_code)
                # self.mailer.send_email(
                #     subject=f"Flight deals to {city}, {country_code}",
                #     message=self.format_flight_deals(data=offers, from_code="LPL", to_code=iata_code),
                # )

    def format_flight_deals(self, data: list, from_code: str, to_code: str) -> None:
        """Format a message containing flight deals.

        Args:
            data (list): List of flight offers (extracted from the API response).
            from_code (str): Origin airport code.
            to_code (str): Destination airport code.

        Returns:
            Formatted message string.

        """
        num_deals = len(data)

        message = (
            f"We found {num_deals} deals for your preferred flight "
            f"from {from_code} to {to_code}:\n\n"
        )

        for idx, deal in enumerate(data, start=1):
            # Extract deal details
            last_ticket_time = deal["lastTicketingDateTime"]
            total_cost = deal["price"]["grandTotal"]
            num_seats = deal["numberOfBookableSeats"]

            # Extract flight segment (assuming only one itinerary and one segment)
            itinerary = deal["itineraries"][0]
            segment = itinerary["segments"][0]

            departure_time = segment["departure"]["at"]
            arrival_time = segment["arrival"]["at"]

            # Formatting date and time from ISO 8601 to readable format
            from datetime import datetime

            dep_dt = datetime.fromisoformat(departure_time)
            arr_dt = datetime.fromisoformat(arrival_time)

            leave_date = dep_dt.strftime("%Y-%m-%d")
            leave_time = dep_dt.strftime("%H:%M")
            arrival_date = arr_dt.strftime("%Y-%m-%d")
            arrival_time = arr_dt.strftime("%H:%M")

            # Append to the message
            message += (
                f"Deal {idx} departs on {leave_date} at {leave_time} "
                f"and arrives on {arrival_date} at {arrival_time}. "
                f"This has a total cost of £{total_cost}. This offer ends on {last_ticket_time} - "
                f"there are {num_seats} seats available.\n\n"
            )

        print(message)
        # return message.strip()
