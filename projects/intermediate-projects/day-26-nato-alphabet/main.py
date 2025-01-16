"""Convert word into Nato alphabet."""

from pathlib import Path

import pandas as pd

nato_phonetic_alphabet_filepath = Path("./nato_phonetic_alphabet.csv")

nato_phonetic_alphabet_df = pd.read_csv(nato_phonetic_alphabet_filepath)

# COMPLETE: 1. Create a dictionary in this format:

alphabet_dict = {row.letter: row.code for (_, row) in nato_phonetic_alphabet_df.iterrows()}

# COMPLETE: 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Enter a word: \n").upper()

user_word_phonetic = [alphabet_dict[letter] for letter in user_word]
print(user_word_phonetic)
