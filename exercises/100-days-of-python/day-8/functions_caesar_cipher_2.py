# Using my original code from functions_caesar_cipher_1

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

text_letters = []
adjusted_index = []


def encrypt(direction, text, shift):
    if direction == "encode":
        for letter in text:
            if letter in alphabet:
                text_letters.append(
                    alphabet.index(letter) + shift
                )  # gets index location of text's letters

        for number in text_letters:
            if number > 25:
                adjusted_index.append(
                    alphabet[(number - number) + (shift - 1)]
                )  # SHOULD
                # reset alphabet to a, so if alphabet[26] occurs with shift=1, z
                # will become a
            else:
                adjusted_index.append(
                    alphabet[number]
                )  # returns shifted letters
        print(f"The encoded text is {''.join(adjusted_index)}.")


def decrypt(direction, text, shift):
    if direction == "decode":
        for letter in text:
            if letter in alphabet:
                text_letters.append(
                    alphabet.index(letter) - (shift)
                )  # gets index location of text's letters
        for number in text_letters:
            adjusted_index.append(alphabet[number])  # returns shifted letters
        print(f"The encoded text is {''.join(adjusted_index)}.")


encrypt(direction, text, shift)
decrypt(direction, text, shift)

# Differences in her code:
# def decrypt(cipher_text, shift_amount)
#   plain_text = ""
#   for letter in cipher_text:
#       position = alphabet.index(letter)
#       new_position = position - shift_amount
# if direction == "encode"
#   encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode"
#   decrypt(cipher_text=text, shift_amount=shift)
