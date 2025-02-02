"""Webscraping Lessons."""

from pathlib import Path

import requests
from blender import Blender
from bs4 import BeautifulSoup

local_page = "./website.html"
remote_page = "https://news.ycombinator.com/"

local_page_content = Path(local_page).read_text()
remote_page_content = requests.get(remote_page, timeout=10).text

soup = BeautifulSoup(remote_page_content, "html.parser")
blender = Blender()


# link content
links = soup.select("td span.titleline a")
# print(f"Links {links}")

links_content = blender.select_elements_content(soup, "td span.titleline > a")
# print(f"Links Content {links_content}")

links_href = blender.select_elements_by_attribute(soup, "td span.titleline > a", "href")
# print(f"Links Href {links_href}")

# scores

scores = [int(score.split()[0]) for score in blender.select_elements_content(soup, "span.score")]
# print(f"Scores {scores}")

link_dict = {}

for index in range(len(links_content)):
    print()
    link_dict[str(index)] = {
        "title": links_content[index],
        "link": links_href[index],
        "upvotes": scores[index],
    }

# highest_score_index = scores.index(max(scores))
highest_score_index = max(enumerate(scores), key=lambda x: x[1])[0]

print(
    f"{links_content[highest_score_index]} has the highest score with {scores[highest_score_index]} upvotes. It links to {links_href[highest_score_index]}"
)
