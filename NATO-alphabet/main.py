import pandas

data = pandas.read_csv("nato_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)


def generate_phonetic():
    user_word = input("Put a word: ").upper()
    try:
        output = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters please!")
        generate_phonetic()
    else:
        print(output)


generate_phonetic()
