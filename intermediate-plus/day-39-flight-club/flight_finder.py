"""Flight finder.

This module contains the FlightFinder class providing methods to search for flight deals.

Public Methods:
    notify_users: Notify users of flight deals.

"""

import datetime as dt

from amadeus import Amadeus
from mailer import Mailer
from sheety import Sheety


class FlightFinder:
    """Flight finder class."""

    def __init__(self) -> None:
        """Construct an instance of FlightFinder."""
        self.sheety = Sheety(project_name="flightDeals")
        self.amadeus = Amadeus()
        self.mailer = Mailer()
        self.destination_data = self.sheety.read("prices")["prices"]
        self.user_data = self.sheety.read("users")["users"]
        self.sanitised_data = []

    def notify_users(self) -> None:
        """Issue flight notifications to users."""
        self._sanitise_data()
        self._flight_search()
        mailing_list = []
        for user in self.user_data:
            mailing_list.append(
                {"name": user["whatIsYourFirstName?"], "email": user["whatIsYourEmailAddress?"]}
            )
        self.mailer._send_mail(recipients=mailing_list, message=self.mailer.message)

    def _sanitise_data(self) -> None:
        """Run the flight search."""
        print("--------------------------")
        print("Sanitising data...")
        for destination in self.destination_data:
            require_update = False
            city = destination["city"]
            country = destination["country"]
            iata_code = destination["iataCode"]
            country_code = destination["countryCode"]
            lowest_price = destination["lowestPrice"]
            id = destination["id"]

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
                self.sheety.update(row=id, data=new_data, sheet="prices")
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
        print("<<< Data sanitised.")

    def _flight_search(self) -> None:
        """Run the flight search."""
        print("--------------------------")
        print("🧐 Looking for flights 🕵️‍♂️...")
        for destination in self.sanitised_data:
            city = destination["city"]
            country_code = destination["country_code"]
            lowest_price = destination["lowest_price"]
            iata_code = destination["iata_code"]

            print(f">>> to {city}, {country_code}, with a maximum price of {lowest_price}")
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
                print(f"<<< Search complete: {len(offers)} offers found.")
                self._format_flight_deals(data=offers, from_code="LPL", to_code=iata_code)
        print(self.mailer.message)

    def _format_flight_deals(self, data: list, from_code: str, to_code: str) -> None:
        """Format a message containing flight deals, handling direct and stopover flights.

        Args:
            data (list): List of flight offers (extracted from the API response).
            from_code (str): Departure airport code.
            to_code (str): Arrival airport code.

        """
        num_deals = len(data)
        message = f"\n{num_deals} flights from {from_code} to {to_code}\n\n"

        for idx, deal in enumerate(data, start=1):
            last_ticket_time = deal["lastTicketingDateTime"]
            total_cost = deal["price"]["grandTotal"]
            num_seats = deal["numberOfBookableSeats"]

            itinerary = deal["itineraries"][0]
            segments = itinerary["segments"]

            first_segment = segments[0]
            last_segment = segments[-1]

            departure_time = first_segment["departure"]["at"]
            arrival_time = last_segment["arrival"]["at"]

            dep_dt = dt.datetime.fromisoformat(departure_time)
            arr_dt = dt.datetime.fromisoformat(arrival_time)

            leave_date = dep_dt.strftime("%Y-%m-%d")
            leave_time = dep_dt.strftime("%H:%M")
            arrival_date = arr_dt.strftime("%Y-%m-%d")
            arrival_time = arr_dt.strftime("%H:%M")

            stop_count = len(segments) - 1

            if stop_count == 0:
                message += (
                    f"👉 Deal {idx}\n\n"
                    f"🛫 departs on {leave_date} at {leave_time}\n"
                    f"🛬 arrives on {arrival_date} at {arrival_time}.\n"
                    f"🚀 Direct! No stops for you!\n"
                    f"💷 The price is £{total_cost}.\n"
                    f"⏰ This offer ends on {last_ticket_time} - "
                    f"there are only {num_seats} seats left.\n\n"
                )
            else:
                stop_airports = [segment["arrival"]["iataCode"] for segment in segments[:-1]]

                message += (
                    f"👉 Deal {idx}\n\n"
                    f"🛫 departs on {leave_date} at {leave_time}\n"
                    f"🛬 arrives on {arrival_date} at {arrival_time}.\n"
                    f"🛑 It has {stop_count} stop{'s' if stop_count > 1 else ''} "
                    f"along the way at {', '.join(stop_airports)}. \n"
                    f"💷 The price is £{total_cost}.\n"
                    f"⏰ This offer ends on {last_ticket_time} - "
                    f"there are {num_seats} seats left.\n\n"
                )

        self.mailer.message += message
