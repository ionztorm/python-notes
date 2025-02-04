"""Get the top 100 tracks from a Billboard page on a given date."""

import requests as req
from blender import Blender
from bs4 import BeautifulSoup


def get_tracks() -> tuple[list[str], str]:
    """Get the top 100 tracks from a Billboard page on a given date.

    Returns:
        list[str]: The list of song titles.

    """
    user_input = input(
        "what year do you want to travel to? enter your date in this format 'YYYY-MM-DD': "
    )

    empire_top_100_url = f"https://www.billboard.com/charts/hot-100/{user_input}/"
    header = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
        )
    }

    blender = Blender()

    empire_top_100_html = req.get(empire_top_100_url, headers=header, timeout=10).text
    soup = BeautifulSoup(empire_top_100_html, "html.parser")
    return (blender.select_elements_content(soup, ".o-chart-results-list__item > h3"), user_input)
