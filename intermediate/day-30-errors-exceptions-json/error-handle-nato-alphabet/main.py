"""Convert word into Nato alphabet."""

from pathlib import Path

import pandas as pd

nato_phonetic_alphabet_filepath = Path("./nato_phonetic_alphabet.csv")

nato_phonetic_alphabet_df = pd.read_csv(nato_phonetic_alphabet_filepath)

alphabet_dict = {row.letter: row.code for (_, row) in nato_phonetic_alphabet_df.iterrows()}

def get_phonetic_values() -> None:
    """Get user input and convert to Nato alphabet."""
    user_word = input("Enter a word: \n").upper()
    try:
        user_word_phonetic = [alphabet_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        get_phonetic_values()
    else:
        print(user_word_phonetic)
