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
        self.email = os.getenv("EMAIL_SENDER")
        self.recipient = os.getenv("EMAIL_RECIPIENT")
        self.password = os.getenv("EMAIL_PASSWORD")
        self.server = e.SMTP("smtp.gmail.com")
        self.message = ""

    def send_mail(self, price: str) -> None:
        """Send an email notification.

        Args:
            price (str): The current price of the item.

        """
        if not self.email or not self.password or not self.recipient:
            raise ValueError("Please set email, password, and recipient environment variables.")

        body = (
            f"Subject: Price Drop!\n\nHey!,\n\nThe price you were watching has dropped to {price}"
        )

        with self.server as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(
                from_addr=self.email, to_addrs=self.recipient, msg=body.encode("utf-8")
            )
            print(">>> Emails sent successfully 📮")
