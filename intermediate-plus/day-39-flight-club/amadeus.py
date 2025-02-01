"""Amadeus flight controller.

This module contains the Amadeus class for handling flight data requests.

Methods:
    get_iata_code: Get the IATA code for a city.
    get_country_code: Get the country code for a country.
    get_flights: Get flight data for a destination.

"""

import os
from typing import TypedDict, Unpack

import requests
from dotenv import load_dotenv, set_key

from api_parent import API

load_dotenv()


class FlightSearch(TypedDict):
    """Kwarg types for flight search."""

    origin: str
    destination: str
    departure_date: str
    adults: int
    max_offers: int
    max_price: int
    currency: str


class Amadeus(API):
    """Amadeus class for flight data requests."""

    def __init__(self) -> None:
        """Construct an instance of the Amadeus class."""
        load_dotenv()
        self.domain = "https://test.api.amadeus.com"
        self.auth_token_endpoint = f"{self.domain}/v1/security/oauth2/token"
        self.cities_endpoint = f"{self.domain}/v1/reference-data/locations/cities"
        self.country_code_endpoint = "https://restcountries.com/v3.1/name"
        self.flight_offers_endpoint = f"{self.domain}/v2/shopping/flight-offers"
        self.client_id: str = os.getenv("AMADEUS_KEY", "")
        self.client_secret: str = os.getenv("AMADEUS_SECRET", "")
        self.bearer: str = self._get_auth_token()
        self.headers = {"Authorization": f"Bearer {self.bearer}"}

    def _get_auth_token(self, refresh: bool = False) -> str:
        """Get the Amadeus auth token.

        Args:
            refresh (bool): Whether to refresh the token.

        Returns:
            str: The bearer token.

        """
        token = os.getenv("AMADEUS_BEARER_TOKEN", "")

        if not refresh and token:
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
        """Retreive location data by city.

        Args:
            city (str): The city name.
            country_code (str): The country code.
            max (int): The maximum number of results to return.
            include (list[str]): The data to include in the response.

        Returns:
            str: The IATA code for the city.

        """
        parameters = {"keyword": city, "countryCode": country_code, "max": max, "include": include}

        token_expired = True
        while token_expired:
            response = self.handle_request(
                requests.get,
                skip=True,
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

        print(response["data"][0]["iataCode"])
        return response["data"][0]["iataCode"]

    def get_country_code(self, country: str) -> str:
        """Get country code for a given country.

        Args:
            country (str): The full country name, e.g., "United Kingdom"

        Returns:
            str: The country code

        """
        url = f"{self.country_code_endpoint}/{country}?fullText=true"
        country_data = self.handle_request(requests.get, url=url, timeout=5)

        if not country_data:
            raise ValueError("Failed to retrieve country code.")

        return country_data["cca2"]

    def get_flights(self, **kwargs: Unpack[FlightSearch]) -> list:
        """Get flights for destination.

        Args:
            kwargs (Unpack[FlightSearch]): Flight search parameters.
            Accepts origin, destination, departure_date, adults, max_offers, max_price, currency.

        Returns:
            list[str]: flights

        """
        parameters = {
            "originLocationCode": kwargs["origin"],
            "destinationLocationCode": kwargs["destination"],
            "departureDate": kwargs["departure_date"],
            "adults": kwargs["adults"],
            "currencyCode": kwargs["currency"],
            "max": kwargs["max_offers"],
            "maxPrice": kwargs["max_price"],
        }

        token_expired = True
        while token_expired:
            response = self.handle_request(
                requests.get,
                skip=True,
                url=f"{self.domain}/v2/shopping/flight-offers",
                params=parameters,
                headers=self.headers,
                timeout=60,
            )

            if "errors" in response and response["errors"][0]["status"] == 401:
                print("Token expired, refreshing.")
                self._get_auth_token(refresh=True)
            else:
                token_expired = False
        return response["data"]
