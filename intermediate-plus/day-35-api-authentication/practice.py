"""Weather API Practice."""

import os
import smtplib

import requests
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
TO_EMAIL = os.environ.get("TO_EMAIL")
api_key = os.environ.get("API_KEY")
city = "Liverpool"
weather_url = "http://api.openweathermap.org/data/2.5/weather"
hourly_url = "http://pro.openweathermap.org/data/2.5/forecast/hourly"
geo_url = "http://api.openweathermap.org/geo/1.0/direct"
five_day_url = "http://api.openweathermap.org/data/2.5/forecast"
if api_key is None:
    raise ValueError("API_KEY environment variable is not set")

params: dict[str, str] = {"q": city, "appid": api_key}


def get_data(url: str, params: dict, tmout: int) -> dict:
    """Get the data from the API."""
    response: requests.Response = requests.get(url, params=params, timeout=tmout)
    response.raise_for_status()
    return response.json()


def get_location() -> tuple[str, str]:
    """Get the location of the user."""
    response: requests.Response = requests.get(geo_url, params=params, timeout=5)
    response.raise_for_status()
    data = response.json()
    return data[0]["lat"], data[0]["lon"]


def should_take_umbrella() -> bool:
    """Get the five day forecast."""
    lat, lon = get_location()
    five_day_forecast_params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "cnt": 4,  # number of timestamps - default is 40
    }
    data = get_data(five_day_url, five_day_forecast_params, 5)
    forecasts = data["list"]
    should_take_umbrella = False
    for forecast in forecasts:
        if forecast["weather"][0]["id"] < 700:
            should_take_umbrella = True
            break
    return should_take_umbrella


def send_email() -> None:
    """Send an email."""
    if EMAIL is None or PASSWORD is None:
        raise ValueError("Email or password environment variables are not set")
    if TO_EMAIL is None:
        raise ValueError("TO_EMAIL environment variable is not set")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=TO_EMAIL,
            msg=(
                "Subject:Bring an umbrella\n\n"
                "It's going to rain today. Don't forget to bring an umbrella."
            ),
        )


def main() -> None:
    """Run the main function."""
    send_email() if should_take_umbrella() else None


main()
