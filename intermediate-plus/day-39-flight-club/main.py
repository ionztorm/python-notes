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
        city = destination["city"]
        country = destination["country"]  # noqa: F841
        country_code = destination["countryCode"] if destination["countryCode"] else None
        iata_code = destination["iataCode"] if destination["iataCode"] else None  # noqa: F841
        # TODO: 1: if no country code, get country code
        # TODO: 2: if no iata code, get iata code
        if not destination["iataCode"]:
            amadeus.get_iata_code(city=city, country_code=country_code)
        # TODO: 3: update (PUT) sheet
        # TODO: 4: flight search
        print(destination)


main()
