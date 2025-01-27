"""Perform calculations on stock data."""

def get_open_price(data: dict, date: str) -> float:
    """Get the opening price of the stock."""
    return float(data["Time Series (Daily)"][date]["1. open"])

def get_close_price(data: dict, date: str) -> float:
    """Get the closing price of the stock."""
    return float(data["Time Series (Daily)"][date]["4. close"])


def calc_open_close_diff(open_price: float, close_price: float) -> float:
    """Calculate the difference between the open and close prices."""
    return close_price - open_price

def calc_close_price_diff(start_price: float, end_price: float) -> tuple[float, float]:
    """Calculate the difference between two closing prices."""
    diff = end_price - start_price
    percent_diff = (diff / end_price) * 100
    return diff,  percent_diff

def get_close_prices_comparison(data: dict) -> dict:
    """Get the difference and percentage difference between two closing prices."""
    stocks = [value for (_, value) in data["Time Series (Daily)"].items()]
    dates = [key for (key, _) in data["Time Series (Daily)"].items()]
    start_close = float(stocks[0]["4. close"])
    end_close = float(stocks[1]["4. close"])
    close_diff, percent_diff = calc_close_price_diff(start_close, end_close)
    return {
            "start_date": dates[0],
            "end_date": dates[1],
            "start_value": start_close,
            "end_value": end_close,
            "close_diff": close_diff,
            "percent_diff": percent_diff,
            "pos_diff": abs(close_diff),
            "pos_per": abs(percent_diff),
            "direction": "Increased" if close_diff > 0 else "Decreased"
            }
