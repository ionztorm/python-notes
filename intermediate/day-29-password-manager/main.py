"""Password Manager."""

import tkinter as tk
from pathlib import Path
from random import choice, randint, shuffle
from tkinter import messagebox

import pyperclip

LOGO_PATH = Path("logo.png")


def copy(text: str) -> None:
    """Copy text to clipboard."""
    pyperclip.copy(text)

def clear_inputs() -> None:
    """Clear inputs."""
    input_website.delete(0, tk.END)
    input_email_user.delete(0, tk.END)
    input_password.delete(0, tk.END)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password() -> None:
    """Generate a password."""
    password_list = (
        [choice(letters) for _ in range(randint(8,10))] +
        [choice(symbols) for _ in range(randint(2,4))] +
        [choice(numbers) for _ in range(randint(2,4))]
    )
    shuffle(password_list)
    password = "".join(password_list)
    input_password.delete(0, tk.END)
    input_password.insert(0, password)
    copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password() -> None:
    """Save password to file."""
    website = input_website.get()
    email = input_email_user.get()
    password = input_password.get()
    data = f"{website} | {email} | {password}\n"

    if not website or not email or not password:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:

        confirmation_message = (
                f"You are saving:\n"
                f"Website: {website}\n"
                f"Email: {email}\n"
                f"Password: {password}\n"
                "Ok to continue?"
                )

        confirmation = messagebox.askokcancel(title=website, message=confirmation_message)

        if confirmation:
            file_path = Path("passwords.txt")
            if not file_path.exists():
                file_path.touch()

            with file_path.open("a") as file:
                file.write(data)

            clear_inputs()

# ---------------------------- UI SETUP ------------------------------- #

root = tk.Tk()
root.title("Password Manager")
root.config(padx=20, pady=20)

root.grid_columnconfigure(0, weight=0)  # Prevent stretching for the first column
root.grid_columnconfigure(1, weight=1)  # Allow the second column to stretch
root.grid_columnconfigure(2, weight=0)

# Canvas
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
bg_img = tk.PhotoImage(file=LOGO_PATH)
canvas.create_image(100, 100, image=bg_img)
canvas.grid(column=0, row=0,columnspan=3, sticky="")

# elements
label_website = tk.Label(text="Website:", justify="left", anchor="w", width=12)
label_email_user = tk.Label(text="Email/Username:", justify="left", anchor="w")
label_password = tk.Label(text="Password:", justify="left", anchor="w")

button_generate_password = tk.Button(
        text="Generate Password", command=generate_password, highlightthickness=0
        )
button_add = tk.Button(text="Add", command=save_password, highlightthickness=0)

input_website = tk.Entry(width=38)
input_email_user = tk.Entry(width=38)

input_password = tk.Entry(width=21)

# grid positioning
label_website.grid(column=0, row=1, sticky="w")
label_email_user.grid(column=0, row=2, sticky="w")
label_password.grid(column=0, row=3, sticky="w")

button_generate_password.grid(column=2, row=3, sticky="e")
button_add.grid(column=1, row=4, columnspan=2, sticky="ew")

input_website.grid(column=1, row=1, columnspan=2, sticky="w")
input_email_user.grid(column=1, row=2, columnspan=2, sticky="w")
input_password.grid(column=1, row=3, sticky="w")

root.mainloop()
