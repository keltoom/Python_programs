# TODO: Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()

# for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()
    # Replace the [name] placeholder with the actual name.
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace("[name]", stripped_name)
        print(new_letter)
        # Save the letters in the folder "ReadyToSend".
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt") as output:
            output.write(new_letter)
