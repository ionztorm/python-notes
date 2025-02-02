"""Webscraping lesson project: 100 greatest movies of all time."""

from pathlib import Path

import requests
from blender import Blender
from bs4 import BeautifulSoup

webpage = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/",
    timeout=10,
).text

document = Path("top-100-movies.txt")

if not document.exists():
    document.touch()

soup = BeautifulSoup(webpage, "html.parser")
blender = Blender()

movies = blender.select_elements_content(soup, "h3.title")[::-1]

with document.open("a") as file:
    file.writelines(f"{movie}\n" for movie in movies)
    print("Written")


print(document.read_text())
