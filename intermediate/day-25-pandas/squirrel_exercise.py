"""Squirrel Dat Exercise.

Goal:
    Create a new DataFrame containing the Fur, Color, and Count.
"""

from pathlib import Path

import pandas as pd

squirrel_data_path = Path("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Create DataFrame from CSV
squirrel_df = pd.read_csv(squirrel_data_path)

print(squirrel_df)

fur_colors = squirrel_df["Primary Fur Color"]
unique_fur_colors = fur_colors.dropna().unique()
count_list = fur_colors.value_counts().to_list()

print(unique_fur_colors)
print(count_list)

fur_dict = {
        "Fur Color": unique_fur_colors,
        "Count": count_list
        }

fur_df = pd.DataFrame(fur_dict)
fur_df.to_csv("fur_count.csv")
