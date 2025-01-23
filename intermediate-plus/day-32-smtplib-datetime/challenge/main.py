"""SMTP lib practice."""

import datetime as dt
import os
import secrets
import smtplib
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

quotes_file = Path("quotes.txt")
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_of_emails = "Thursday"

my_email = os.getenv("my_email")
to_email = os.getenv("to_email")
my_password = os.getenv("my_password")

# ---------------------------- Setup Email ----------------------------

def send_email(quote: str) -> None:
    """Send an email."""
    if my_email is None:
        raise ValueError("Environment variable 'my_email' is not set.")
    if to_email is None:
        raise ValueError("Environment variable 'to_email' is not set.")
    if my_password is None:
        raise ValueError("Environment variable 'my_password' is not set.")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject:Quote of the Day\n\n{quote}"
                )

# ---------------------------- Get Quote ----------------------------

def get_quote() -> str:
    """Select a random quote from a list."""
    if not quotes_file.exists():
        raise FileNotFoundError("No quotes file found.")

    if quotes_file.stat().st_size == 0:
        raise ValueError("Quotes file is empty.")

    if not len(quotes_file.read_text().splitlines()):
        raise ValueError("Quotes file is empty.")

    list_of_quotes = quotes_file.read_text().splitlines()
    return secrets.choice(list_of_quotes)

# ---------------------------- Get Date ------------------------------

def get_date() -> int:
    """Get current day."""
    return dt.datetime.now().weekday()

# ---------------------------------------------------------------------

def main() -> None:
    """Entry point."""
    today = days[get_date()]

    if today == day_of_emails:
        try:
            send_email(get_quote())
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)
    else:
        print(f"Today is {today}, we only send emails on Mondays.")


main()
