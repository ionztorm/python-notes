"""Flashcard app for learning new words in a foreign language."""

import secrets
import tkinter as tk
from pathlib import Path
from tkinter import messagebox

import pandas as pd

# ---------------------------- CONSTANTS ------------------------------- #


BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT_IMAGE_FILE = Path("./images/card_front.png")
CARD_BACK_IMAGE_FILE = Path("./images/card_back.png")
GREEN_TICK_FILE = Path("./images/right.png")
RED_CROSS_FILE = Path("./images/wrong.png")
DATA_FILE = Path("./data/french_words.csv")
WORDS_TO_LEARN_FILE = Path("./data/words_to_learn.csv")
CHANGE_TIME = 3000


if not DATA_FILE.exists() and not WORDS_TO_LEARN_FILE.exists():
    messagebox.showerror("Error", "Data file not found.")
    exit()

try:
    data = pd.read_csv(WORDS_TO_LEARN_FILE)
except FileNotFoundError:
    data = pd.read_csv(DATA_FILE)
    words_dict = data.to_dict(orient="records")
except pd.errors.EmptyDataError:
    data = pd.read_csv(DATA_FILE)
    words_dict = data.to_dict(orient="records")
else:
    words_dict = data.to_dict(orient="records")



# ---------------------------- DATA SETUP ------------------------------- #


data = {}
flip_timer = None
current_word = {}

def next_word() -> None:
    """Get the next word."""
    global flip_timer, current_word

    if flip_timer:
        window.after_cancel(flip_timer)

    if not len(words_dict):
        messagebox.showinfo("Success", "You have learned all the words.")
        exit()


    current_word = secrets.choice(words_dict)

    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_word["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front_image)

    flip_timer = window.after(CHANGE_TIME,flip_card, current_word)

def flip_card(current_word: dict) -> None:
    """Flip the card to show the English translation."""
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(title_text, text="English",fill="white")
    canvas.itemconfig(word_text, text=current_word["English"], fill="white")

def learned_word() -> None:
    """Remove the learned word from the list."""
    words_dict.remove(current_word)
    df = pd.DataFrame(words_dict)
    df.to_csv(WORDS_TO_LEARN_FILE, index=False)
    next_word()

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


card_front_image = tk.PhotoImage(file=CARD_FRONT_IMAGE_FILE)
card_back_image = tk.PhotoImage(file=CARD_BACK_IMAGE_FILE)
right_image = tk.PhotoImage(file=GREEN_TICK_FILE)
wrong_image = tk.PhotoImage(file=RED_CROSS_FILE)


canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(row=0,column=0, columnspan=2)


button_correct = tk.Button(
        image=right_image,
        highlightthickness=0,
        borderwidth=0,
        command=learned_word
        )
button_incorrect = tk.Button(
        image=wrong_image,
        highlightthickness=0,
        borderwidth=0,
        command=next_word
        )

button_correct.grid(row=1, column=0)
button_incorrect.grid(row=1, column=1)

next_word()

window.mainloop()
