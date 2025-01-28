"""Habbit tracker."""

import datetime
import os

import requests
from dotenv import load_dotenv

load_dotenv()

# Constants
PIXELA_ENDPOINT = os.getenv("PIXELA_ENDPOINT")
USER_TOKEN = os.getenv("USER_TOKEN")
USERNAME = os.getenv("USERNAME")
GRAPH_ID = os.getenv("GRAPH_ID")
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/"
PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

if not all([PIXELA_ENDPOINT, USER_TOKEN, USERNAME, GRAPH_ID]):
    raise ValueError("Please check your environment variables.")
"""
# Create a user - only run once
user_params = {
    "token": USER_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=PIXELA_ENDPOINT, json=user_params, timeout=5)
print(respossnse.text)
"""

headers = {
    "X-USER-TOKEN": USER_TOKEN,
}

graph_params = {
    "id": GRAPH_ID,
    "name": "Walking or Cycling",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
"""
respossnseponse = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers, timeout=5)
readable_response = response.json()
if readable_response["isSuccess"] == "false":
    print(readable_response["message"])
else:
    print(
        f"Graph created successfully. View at: {PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}.html"
        )

"""

todays_date = datetime.datetime.now().strftime("%Y%m%d")

pixel_config = {
    "date": todays_date,
    "quantity": "24.4",
}
pixel_response = requests.post(url=PIXEL_ENDPOINT, json=pixel_config, headers=headers, timeout=5)
readable_pixel_response = pixel_response.json()

if readable_pixel_response["isSuccess"] == "false":
    print(readable_pixel_response["message"])
else:
    print(f"Graph updated: {PIXEL_ENDPOINT}.html")
