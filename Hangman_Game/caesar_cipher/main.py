from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
    #fix the code to keep the number/symbol/space when the text is encoded/decoded
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text+=char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

print(logo)

should_continue=True
while should_continue:
  # ask the user if they want to restart the cipher program 
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  #if the user enters a shift that is greater than the number of letters in the alphabet
  shift=shift % 25
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  result=input("Type 'yes' if you want to go agin.Otherwise type 'no'\n")
  if result=='no':
    should_continue=False
    print('Goodbye')