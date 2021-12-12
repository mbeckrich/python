import art

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
]

print(f"{art.logo}")


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char not in alphabet:
            alphabet.append(char)
        position = alphabet.index(char)
        if position >= 26:
            position -= shift_amount
        new_position = position + shift_amount
        if new_position > len(alphabet):
            new_position %= len(alphabet)
        end_text += alphabet[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}")


rerun = "yes"
while rerun == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(
        start_text=text,
        shift_amount=shift,
        cipher_direction=direction,
    )

    rerun = input(
        "Would you like to use the cipher again? Type 'yes' or 'no.' "
    )
