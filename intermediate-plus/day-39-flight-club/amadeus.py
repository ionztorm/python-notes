"""Amadeus flight controller."""

import os

import requests
from api_parent import API
from dotenv import load_dotenv, set_key

load_dotenv()


class Amadeus(API):
    """Amadeus class for flight data requests."""

    def __init__(self) -> None:
        """Construct an instance of the Amadeus class."""
        load_dotenv()
        self.domain = "https://test.api.amadeus.com"
        self.auth_token_endpoint = f"{self.domain}/v1/security/oauth2/token"
        self.cities_endpoint = f"{self.domain}/v1/reference-data/locations/cities"
        self.client_id: str = os.getenv("AMADEUS_KEY", "")
        self.client_secret: str = os.getenv("AMADEUS_SECRET", "")
        self.bearer: str = self._get_auth_token()
        self.headers = {"Authorization": f"Bearer {self.bearer}"}

    def _get_auth_token(self, refresh: bool = False) -> str:
        """Get the Amadeus auth token."""
        token = os.getenv("AMADEUS_BEARER_TOKEN", "")

        if not refresh:
            if token:
                return token

        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        header = {"Content-Type": "application/x-www-form-urlencoded"}

        token = self.handle_request(
            requests.post, url=self.auth_token_endpoint, headers=header, data=data, timeout=5
        )["access_token"]

        if not token:
            raise ValueError("Failed to retrieve access token.")

        print("New token recieved")

        set_key(".env", "AMADEUS_BEARER_TOKEN", token)

        load_dotenv(override=True)
        self.headers = {"Authorization": f"Bearer {token}"}
        return token

    def get_iata_code(
        self,
        city: str,
        country_code: str | None = None,
        max: int | None = None,
        include: list[str] | None = None,
    ) -> str:
        """Retreive location data by city."""
        # TODO: remove later.
        country_code = "GB"
        parameters = {"keyword": city, "countryCode": country_code, "max": max, "include": include}

        token_expired = True
        while token_expired:
            response = self.handle_request(
                requests.get,
                url=self.cities_endpoint,
                params=parameters,
                headers=self.headers,
                timeout=5,
            )

            if "errors" in response and response["errors"][0]["status"] == 401:
                print("Token expired, refreshing.")
                self._get_auth_token(refresh=True)
            else:
                token_expired = False

        return response["data"][0]["iataCode"]

    def get_country_code(self, country: str) -> str:
        """Get country code for a given country.

        Args:
            country (str): The full country name, e.g., "United Kingdom"

        Returns:
            str: The country code

        """
        # TODO: finish.
        return country

    def get_flights(self) -> None:
        """Get flights for destination.

        Args:
            args...

        Returns:
            list[str]: flights

        """
        pass
