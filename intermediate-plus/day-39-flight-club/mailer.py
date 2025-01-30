"""Mailer controller for email notifications."""

import smtplib as e


class Mailer:
    """Mailer class for issuing email notifications."""

    def __init__(self) -> None:
        """Construct an instance of the mailer class."""
        self.from_mail = ""

    def send_mail(self, recipient: str) -> None:
        """Send an email notification."""
        pass
