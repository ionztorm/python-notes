"""Parent class for API inheritance.

This class provides a method to handle API requests and errors.

Methods:
    handle_request: Execute an API request and handle any errors.

"""

from typing import Any, Callable, NotRequired, TypedDict, Unpack

import requests


class RequestKwargs(TypedDict):
    """TypedDict for kwargs type."""

    url: str
    json: NotRequired[dict]
    data: NotRequired[dict]
    params: NotRequired[dict]
    headers: NotRequired[dict]
    timeout: int


class API:
    """API parent for utility fuction inheritance."""

    @staticmethod
    def handle_request(
        api_call: Callable, skip: bool = False, **kwargs: Unpack[RequestKwargs]
    ) -> dict[str, Any]:
        """Execute an API request and handles any errors.

        Args:
            api_call (Callable): A function that performs an API request, for example, requsts.get.
            skip (bool): Whether to skip error handling. Default is False. Used when you want to
                handle errors manually.
            **kwargs: Keyword arguments to pass to the request function.

        Returns:
            dict: The JSON respons from the API call.

        Raises:
            ValueError: If the response does not contain valid JSON.
            requests.RequestException: For network or request failures.

        """
        try:
            response = api_call(**kwargs)
            if not skip:
                response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return data[0]

            return data

        except requests.Timeout as e:
            raise requests.RequestException("Request timed out. Please try again.") from e

        except requests.ConnectionError as e:
            raise requests.RequestException("Network error. Check your internet connection.") from e

        except requests.JSONDecodeError as e:
            raise ValueError("Invalid JSON response from the API.") from e

        except requests.RequestException as e:
            raise requests.RequestException(f"API request failed: {e}") from e
