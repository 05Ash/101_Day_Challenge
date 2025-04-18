import os
import pandas as pd

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "nato_phonetic_alphabet.csv")

nato_df = pd.read_csv(file_path)

nato_dict = {row.letter: row.code for row in nato_df.itertuples()}

word = input("Enter a word: ").upper()

result = [nato_dict[char] for char in word]

print(result)
