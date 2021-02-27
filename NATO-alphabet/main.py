import pandas

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Put a word: ").upper()

output = [nato_dict[letter] for letter in user_word]
print(output)
