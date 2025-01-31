"""Flight club."""

from amadeus import Amadeus
from dotenv import load_dotenv
from mailer import Mailer
from sheety import Sheety

load_dotenv()


sheety = Sheety(project_name="flightDeals", sheet_name="prices")
amadeus = Amadeus()
mailer = Mailer()


# TODO: Create program class


def main() -> None:
    """Execute program."""
    destination_list = sheety.read()["prices"]
    for destination in destination_list:
        require_update = False
        row_id = destination["id"]
        city = destination["city"]
        country = destination["country"]
        country_code = destination["countryCode"] if destination["countryCode"] else None
        iata_code = destination["iataCode"] if destination["iataCode"] else None

        # TODO: 2: if no country code, get country code
        if not country_code:
            require_update = True
            print("No country code found -> Searching")
            country_code = amadeus.get_country_code(country=country)
            if country_code:
                print(f"Country code found: {country_code}")
        # TODO: 1: if no iata code, get iata code
        if not iata_code:
            require_update = True
            print("No IATA code found -> Searching")
            iata_code = amadeus.get_iata_code(city=city, country_code=country_code)
            if iata_code:
                print(f"IATA code found: {iata_code}")
        # TODO: 3: update (PUT) sheet
        if require_update:
            new_data = {
                "price": {
                    "iataCode": iata_code,
                    "countryCode": country_code,
                }
            }
            print("Updating sheet...")
            sheety.update(row=row_id, data=new_data)
            print("Sheet updated.")
        # TODO: 4: flight search
        print(destination)


main()
