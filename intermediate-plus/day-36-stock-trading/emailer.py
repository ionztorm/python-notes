"""Email management."""

import os
import smtplib

from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def send_email(recipient: str, message: str) -> None:
    """Send an email to the recipient."""
    if not EMAIL or not PASSWORD:
        raise ValueError("Please set EMAIL and PASSWORD environment variables.")


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=recipient,
            msg=message
            )
