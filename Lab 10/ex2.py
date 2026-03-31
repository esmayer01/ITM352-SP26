# Create a dataframe from individual lists
# Do some simple statistics on the data
from tkinter.font import names


import pandas as pd

# List of individuals' ages
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45  ]

# Lists of individual' names and genders
Names = ["Joe", "Jaden", "Max", "Sidney", "Evengi", "Taylor", "Pia", "Luis", "Bianca", "Cyndi"]
Gender = ["M", "M", "M", "F", "F", "F", "F", "M", "F", "F"]

# Create a dictionary from the lists of ages and genders
dict = zip(ages, Gender)
print(list(dict))

# Create a DataFrame from the dictionary
df = pd.DataFrame(dict, index=names, columns=["Age", "Gender"])
print(df)

summary = df.describe()
print(summary)
