"""Send an email to someone on their birthday."""

import datetime as dt
import os
import secrets
import smtplib as email
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

bithdays_file = Path("birthdays.csv")

my_email = os.getenv("my_email")
my_password = os.getenv("my_password")

print(my_email, my_password)


# ---------------------------- Get Birthdays ----------------------------

def get_birthday_list() -> dict:
    """Read the birthdays.csv file and return a list of dictionaries."""
    birthdays_df = pd.read_csv(bithdays_file)
    return {
            (data_row.month, data_row.day):
                data_row for (_, data_row) in birthdays_df.iterrows()
            }

# could also use:
# return birthdays_df.to_dict(orient="records")
# but would need to change the check_birthday function to check
# day and month separately

# ---------------------------- Get Date ----------------------------------

def get_today_day_and_month() -> tuple[int, int]:
    """Return the current day and month."""
    return (dt.datetime.now().month, dt.datetime.now().day)

# ---------------------------- Check Birthday ----------------------------

def check_birthday(birthdays: dict, today: tuple) -> list[dict]:
    """Check if today matches a birthday in the birthdays.csv."""
    return [person for date, person in birthdays.items() if date == today]

# ---------------------------- Generate Letter ----------------------------

def generate_letter(person: dict) -> str:
    """Pick a random letter and replace the [NAME] with the person's name."""
    letter = Path(f"./letter_templates/letter_{secrets.randbelow(4)}.txt").read_text()
    return letter.replace("[NAME]", person["name"])

# ---------------------------- Send Email --------------------------------

def send_email(person: dict) -> None:
    """Send the email."""
    if my_email is None:
        raise ValueError("Environment variable 'EMAIL' is not set.")
    if my_password is None:
        raise ValueError("Environment variable 'EMAIL_PASSWORD' is not set.")

    letter = generate_letter(person)
    with email.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=person["email"],
            msg=f"Subject:Happy Birthday\n\n{letter}"
            )

# ---------------------------- Main ---------------------------------------

def main() -> None:
    """Entry point."""
    birthdays = get_birthday_list()
    today = get_today_day_and_month()
    birthday_people = check_birthday(birthdays, today)

    if len(birthday_people):
        for person in birthday_people:
            send_email(person)
    else:
        print("No birthdays today.")

main()
