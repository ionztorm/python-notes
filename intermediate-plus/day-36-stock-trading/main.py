"""Stock checker."""

import os

import fetcher as f
import stock_calculations as sc
from data import data
from dotenv import load_dotenv
from emailer import send_email

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
STOCK_SYMBOL = "IBM"
ALPHA_BASE_API_KEY = os.getenv("ALPHA_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
ALPHA_BASE_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"
ALPHA_BASE_PARAMS = {
    "apikey": ALPHA_BASE_API_KEY,
    "symbol": STOCK_SYMBOL,
    "function": "TIME_SERIES_DAILY",
}
NEWS_PARAMS = {
    "apikey": NEWS_API_KEY,
    "qInTitle": STOCK_SYMBOL,
    "language": "en",
}


def main() -> None:
    """Execute main."""
    # stock_data = f.fetch(url=ALPHA_BASE_URL, params=ALPHA_BASE_PARAMS, timeout=5)  # noqa: ERA001
    stock_data = data

    comparison = sc.get_close_prices_comparison(stock_data)
    print(
        f"The stock price of {STOCK_SYMBOL} has {comparison['direction']} "
        f"by {comparison['pos_diff']:.2f} USD "
        f"({comparison['percent_diff']:.2f}%) from ${comparison['start_value']} on "
        f"{comparison['start_date']} "
        f"to ${comparison['end_value']} on {comparison['end_date']}."
    )

    if comparison["pos_per"] > 0.2:
        print("The stock price has changed significantly. Here are 3 news articles.")
        # func returns a dictionary with key "articles" which is a list of dictionaries
        # slice the list to get the first 3 articles
        articles = f.fetch(NEWS_URL, NEWS_PARAMS, timeout=5)["articles"][:3]
        print("News articles:")
        print("\n".join([f"{article['title']}: {article['url']}" for article in articles]))
        print("\n")
        send_by_email = input("Would you like to recieve these articles via email? (y/n)")
        if send_by_email.lower() == "y":
            recipient = input("Enter your email address: ")
            message = f"Subject: {STOCK_SYMBOL} News\n\n" + "\n".join(
                [
                    f"{article['title']}:\n"
                    f"{article['description'] if article['description'] else 'No description provided.'}"  # noqa: E501
                    f"\n"
                    f"\n"
                    f"\n {article['url']}"
                    for article in articles
                ]
            )

            send_email(recipient, message)
            print(f"Email sent to {recipient}")


main()
