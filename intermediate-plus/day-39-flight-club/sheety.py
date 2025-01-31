"""Sheety class.

This class provides methods to interact with the Sheety API.

Methods:
    create: Create a new entry in a Google Sheet using Sheety api.
    read: Get data from Google Sheet via Sheety api.
    update: Update data in a Google Sheet using the Sheety api.

"""

import os  # noqa: I001

import requests
from dotenv import load_dotenv

from api_parent import API

load_dotenv()


class Sheety(API):
    """Sheety class."""

    def __init__(
        self,
        project_name: str,
        timeout: int = 5,
    ) -> None:
        """Construct an instance of Sheety."""
        self.project: str = project_name
        self.username: str = os.getenv("SHEETY_USERNAME", "")
        self.bearer: str = os.getenv("SHEETY_BEARER", "")

        if not self.bearer:
            raise ValueError("SHEETY_BEARER environment variable is missing or empty.")

        self.headers: dict = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.bearer}",
        }
        self.domain: str = "https://api.sheety.co"
        self.endpoint: str = f"{self.domain}/{self.username}/{self.project}/"
        self.timeout: int = timeout

    def create(self, data: dict, sheet: str) -> dict:
        """Create a new entry in a Google Sheet using Sheety api.

        Args:
            data: dict: a dictionary containing the new data.
            sheet: str: the name of the sheet to update.

        Returns:
            dict: the response from the API.

        """
        if not isinstance(data, dict) or not data:
            raise ValueError("Data is required and must be a dictionary.")
        if not isinstance(sheet, str) or not sheet:
            raise ValueError("Sheet is required and must be a string.")

        return self.handle_request(
            requests.post,
            url=f"{self.endpoint}{sheet}",
            json=data,
            headers=self.headers,
            timeout=self.timeout,
        )

    def read(self, sheet: str) -> dict:
        """Get data from Google Sheet via Sheety api.

        Args:
            sheet: (str) the name of the sheet to read

        Returns:
            dict: the response from the API.

        """
        return self.handle_request(
            requests.get,
            url=f"{self.endpoint}{sheet}",
            headers=self.headers,
            timeout=self.timeout,
        )

    def update(self, row: str, data: dict, sheet: str) -> dict:
        """Update data in a Google Sheet using the Sheety api.

        Args:
            row: str: the row id to update.
            data: dict: a dictionary containing the new data.
            sheet: str: the name of the sheet to update.

        Returns:
            dict: the response from the API.

        """
        return self.handle_request(
            requests.put,
            url=f"{self.endpoint}{sheet}/{row}",
            json=data,
            headers=self.headers,
            timeout=self.timeout,
        )
