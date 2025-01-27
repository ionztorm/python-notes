"""Fetcher module for fetching data from the web."""

import requests as req
from dotenv import load_dotenv

load_dotenv()

def fetch(url: str, params: dict, timeout: int = 10) -> dict:
    """Fetch data from the web using requests module."""
    response = req.get(url, params=params, timeout=timeout)
    response.raise_for_status()
    return response.json()
