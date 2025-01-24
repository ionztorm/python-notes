"""Check when the ISS is close to your current position and it is currently dark.

send an email to tell you to look up.
"""

import os
import smtplib
import time
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=10)
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


def fetch_sunrise_sunset() -> tuple[int,int]:
    """Fetch the sunrise and sunset times.

    Returns:
        tuple[int,int]: The sunrise and sunset times.

    """
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, timeout=10)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    return sunrise, sunset

time_now = datetime.now()

def is_close_to_iss() -> bool:
    """Check if the ISS is close to your current position."""
    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5


def is_dark(sunrise: int, sunset: int) -> bool:
    """Check if it is currently dark."""
    return time_now.hour >= sunset or time_now.hour <= sunrise

def send_email() -> None:
    """Send an email to tell you to look up."""
    if not MY_EMAIL or not MY_PASSWORD:
        raise ValueError("Please fill in the email and password in the .env file.")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up\n\nThe ISS is above you in the sky."
        )


# BONUS: run the code every 60 seconds.
def main() -> None:
    """Run the code every 60 seconds."""
    sunrise, sunset = fetch_sunrise_sunset()
    while True:
        if is_close_to_iss() and is_dark(sunrise, sunset):
            send_email()
        time.sleep(60)


