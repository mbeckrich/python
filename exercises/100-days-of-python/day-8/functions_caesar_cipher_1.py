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


def encrypt(text, shift):
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
            adjusted_index.append(alphabet[number])  # returns shifted letters
    print(f"The encoded text is {''.join(adjusted_index)}.")


encrypt(text=text, shift=shift)

# Differences with her code:
# Says to use different parameter names:
# e.g. def encrypt (plain_text, shift_amount)
# plain_text = text, shift_amount=shift
# alphabet.index(letter) -- well, that's easy. :(
# Her function:
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
# Her solution to the 'civilization' problem is to
# just duplicate the alphabet.
