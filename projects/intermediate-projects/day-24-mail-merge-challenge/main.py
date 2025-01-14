"""Mailmerge challeng for 100 Days of Python day 24."""

from pathlib import Path

names_file = Path("./input/names/invite_names.txt")
letter_file = Path("./input/letters/starter_text.txt")

name_list = names_file.read_text().strip().split("\n")

for name in name_list:
    file_name = f"letter_for_{name}.txt"
    letter_content = letter_file.read_text().replace("[name]", name)
    output = Path(f"./output/letters/{file_name}")
    output.write_text(letter_content)

