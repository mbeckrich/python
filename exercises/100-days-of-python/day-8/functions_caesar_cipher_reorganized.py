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


# def caesar(direction, input_text, shift_amount):
#     if direction == "encode":
#         encoded_text = ""
#         for letter in input_text:
#             position = alphabet.index(letter)
#             new_position = position + shift_amount
#             encoded_text += alphabet[new_position]
#         print(f"The encoded text is {encoded_text}.")
#     if direction == "decode":
#         decoded_text = ""
#         for letter in input_text:
#             position = alphabet.index(letter)
#             new_position = position - shift
#             decoded_text += alphabet[new_position]
#         print(f"The decoded text is {decoded_text}.")


# caesar(direction, input_text=text, shift_amount=shift)

# Her code:


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        # if cipher_direction == "encode":
        #     new_position = position + shift_amount
        # cleaner:
        # if cipher_direction == "decode":
        #     shift_amount *= -1
        # but creates a bug because it gets stuck in the for loop
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d is {end_text}.")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
