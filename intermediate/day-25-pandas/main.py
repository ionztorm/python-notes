"""Pandas practice.

New learnings:
    csv package built in allows

Pandas:
    pip install pandas
    pip install pandas-stubs

"""

# import csv
#
# weather_file_path = Path("./weather_data.csv")
# temperatures = []
#
# # This also works: data = csv.reader(weather_file_path.read_text().splitlines())
#
# with weather_file_path.open('r') as file:
#     data = csv.reader(file)
#
#     temperatures = [int(row[1]) for row in data if row[1] != "temp"]
#
#     for row in data:
#         print(row)
#
# print(temperatures)


from pathlib import Path

import pandas as pd

file_path = Path("./weather_data.csv")

# The output type of this pandas function is a DataFrame
data: pd.DataFrame = pd.read_csv(file_path)

print(data)

# We can get the temperatre column from data:
# The type of this is a Series
print(data["temp"])
print(data.temp) # dot notation also works

# We can get the data in a dictionary format from a DataFrame
data_dict = data.to_dict()

print(data_dict)

# We can get the data in a list format from a Series
temp_list = data["temp"].to_list()

# Average temperature using the .mean() method available on Series
average_temp = data["temp"].mean()


# Maximum temperature using the .max() method available on Series
max_temp = data["temp"].max()

# We can access a row rom a data frame.
data[data.day == "Monday"]

# Get the row with the maximum temperature
max_temp_row = data[data.temp == data.temp.max()]

# We can access data from within this row using the same notations:
max_temp_day = max_temp_row.day
max_temp_temp = max_temp_row.temp
max_temp_condition = max_temp_row.condition

monday_temp_c = data[data.day == "Monday"].temp[0] # the data is at index 0
monday_temp_f = monday_temp_c * 9/5 + 32

# Create a data frame from scratch

example_data = {
        "students": ["Leon", "Dawn", "Holly"],
        "scores": [76, 56, 65],
        }

custom_data_frame = pd.DataFrame(example_data)

# we can use this to create a csv file
custom_data_frame.to_csv("example_data.csv")
