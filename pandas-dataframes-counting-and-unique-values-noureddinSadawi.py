import pandas as pd

raw_data = {
        "city": ["Tripoli", "Sydney", "Tripoli", "Rome", "Rome", "Tripoli", "Rome", "Sydney", "Sydney"],
        "rank": ["1st", "2nd", "1st", "2nd", "1st", "2nd", "1st", "2nd", "1st"],
        "score1": [44, 48, 39, 41, 38, 44, 34, 54, 61],
        "score2": [67, 63, 55, 70, 64, 75, 45, 66, 72],
        }

df = pd.DataFrame(raw_data,
                    index = pd.Index(['A','B','C','D','E','F','G','H','I'], name='letter'),
                    columns = pd.Index(['city', 'rank', 'score1', 'score2'], name='attributes')
                    )

# Count the number of times each unique value appears in a certain column
x = pd.value_counts(df['city'])
print(x)


# Count for the entire dataframe
y = df.apply(pd.value_counts).fillna(0)
print(y.city['Rome'])
print(y)


# List all the unique values in a column
# If we want to see what are the unique outlets in the dental_out column, use .unique()
# z = df['city'].unique()
# print(z)

