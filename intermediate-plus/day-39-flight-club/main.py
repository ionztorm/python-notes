"""Flight club."""

from dotenv import load_dotenv
from flight_finder import FlightFinder

load_dotenv()


flights = FlightFinder()


def main() -> None:
    """Execute program."""
    flights.notify_users()


main()
