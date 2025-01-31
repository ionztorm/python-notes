"""Flight club."""

from dotenv import load_dotenv
from flight_finder import FlightFinder

load_dotenv()


flights = FlightFinder()


def main() -> None:
    """Execute program."""
    flights.sanitise_data()
    flights.flight_search()


main()
