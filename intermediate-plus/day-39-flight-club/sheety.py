"""Sheety class."""

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
        sheet_name: str,
        timeout: int = 5,
    ) -> None:
        """Construct an instance of Sheety."""
        self.project: str = project_name
        self.sheet: str = sheet_name
        self.username: str = os.getenv("SHEETY_USERNAME", "")
        self.bearer: str = os.getenv("SHEETY_BEARER", "")

        if not self.bearer:
            raise ValueError("SHEETY_BEARER environment variable is missing or empty.")

        self.headers: dict = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.bearer}",
        }
        self.domain: str = "https://api.sheety.co"
        self.endpoint: str = f"{self.domain}/{self.username}/{self.project}/{self.sheet}"
        self.timeout: int = timeout

    def create(self, data: dict) -> dict:
        """Create a new entry in a Google Sheet using Sheety api."""
        if not isinstance(data, dict) or not data:
            raise ValueError("Data is required and must be a dictionary.")

        return self.handle_request(
            requests.post, url=self.endpoint, json=data, headers=self.headers, timeout=self.timeout
        )

    def read(self) -> dict:
        """Get data from Google Sheet via Sheety api."""
        return self.handle_request(
            requests.get,
            url=self.endpoint,
            headers=self.headers,
            timeout=self.timeout,
        )

    def update(self, row: str, data: dict) -> dict:
        """Update data in a Google Sheet using the Sheety api.

        Args:
            row: str: the row id to update.
            data: dict: a dictionary containing the new data.

        """
        return self.handle_request(
            requests.put,
            url=f"{self.endpoint}/{row}",
            json=data,
            headers=self.headers,
            timeout=self.timeout,
        )
