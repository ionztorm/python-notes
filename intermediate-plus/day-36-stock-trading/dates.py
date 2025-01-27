"""Get dates for stock data."""
import datetime as dt


def get_dates() -> tuple[str, str]:
    """Get the start and end date, considering weekends."""
    today = dt.datetime.now()

    # If today is Monday, get dates for prrevious Friday and Thursday
    if today.weekday() == 0:
        end_date = (today - dt.timedelta(days=3)).strftime("%Y-%m-%d")
        start_date = (today - dt.timedelta(days=4)).strftime("%Y-%m-%d")
    # If today is Tuesday, get dates for yesterday and previous Friday
    elif today.weekday() == 1:
        end_date = (today - dt.timedelta(days=1)).strftime("%Y-%m-%d")
        start_date = (today - dt.timedelta(days=3)).strftime("%Y-%m-%d")
    else:
        end_date = today.strftime("%Y-%m-%d")
        start_date = (today - dt.timedelta(days=1)).strftime("%Y-%m-%d")

    return start_date, end_date
