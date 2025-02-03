"""Webscraping Lessons."""

from bs4 import BeautifulSoup


class Blender:
    """A stateless web scraping utility that operates on provided BeautifulSoup objects."""

    @staticmethod
    def select_elements_content(soup: BeautifulSoup, selector: str) -> list[str]:
        """Select elements using a CSS selector and return their text content.

        Args:
            soup (BeautifulSoup): The soup object to search in.
            selector (str): The CSS selector to use.

        Returns:
            list[str]: List of text contents from matching elements.

        """
        return [el.get_text(strip=True) for el in soup.select(selector)]

    @staticmethod
    def select_elements_by_attribute(
        soup: BeautifulSoup, selector: str, attribute: str
    ) -> list[str | list[str]]:
        """Select elements using a CSS selector and extract a specific attribute.

        Args:
            soup (BeautifulSoup): The soup object to search in.
            selector (str): The CSS selector to find elements.
            attribute (str): The attribute to extract.

        Returns:
            list[str]: List of extracted attribute values.

        """
        return [el.get(attribute, "") for el in soup.select(selector) if el.has_attr(attribute)]
