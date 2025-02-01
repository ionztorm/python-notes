"""Mailer controller for email notifications.

This module contains the Mailer class for issuing email notifications.

"""

import os
import smtplib as e

from dotenv import load_dotenv

load_dotenv()


class Mailer:
    """Mailer class for issuing email notifications."""

    def __init__(self) -> None:
        """Construct an instance of the mailer class."""
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        self.server = e.SMTP("smtp.gmail.com")
        self.message = ""

    def _send_mail(self, recipients: list[dict], message: str) -> None:
        """Send an email notification.

        Args:
            recipients (list[dict]): A list of recipients.
            message (str): The message to send.

        """
        if not self.email or not self.password:
            raise ValueError("Please set EMAIL and PASSWORD environment variables.")

        with self.server as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            for recipient in recipients:
                body = (
                    f"Subject: Flight Deals are in!\n\nHey {recipient['name']},\n\n"
                    f"Check out these mind blowing deals, and don't miss out! Here's what we found:"
                    f"\n\n{message}"
                )
                connection.sendmail(
                    from_addr=self.email, to_addrs=recipient["email"], msg=body.encode("utf-8")
                )
            print(">>> Emails sent successfully 📮")
