# Password Generator Project -- Do not use as an actual password generator!
import random

letters = [
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
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# # This is the 'hard' way, but does not use any for loops.

# letters_string = "".join(random.choices(letters, k=nr_letters))
# symbols_string = "".join(random.choices(symbols, k=nr_symbols))
# numbers_string = "".join(random.choices(numbers, k=nr_numbers))

# combined_passwords = letters_string + symbols_string + numbers_string

# final_password = "".join(
#     random.sample(combined_passwords, len(combined_passwords))
# )

# print(f"Your new password is: {final_password}.")

# # This uses for loops a bit more.

# combine_string_1 = ""
# for letter in letters_string:
#     combine_string_1 += letter

# combine_string_2 = ""
# for symbol in symbols_string:
#     combine_string_2 += symbol

# combine_string_3 = ""
# for number in numbers_string:
#     combine_string_3 += number

# combined_passwords2 = combine_string_1 + combine_string_2 + combine_string_3
# final_password2 = "".join(
#     random.sample(combined_passwords2, len(combined_passwords2))
# )

# print(f"Your new password is: {final_password2}.")

# Cleaned up version of second approach that generates without user input.

generate_password = input("Press enter to receive a randomized password. ")

password_list = []
for char in range(random.randint(3, len(letters) - 37)):
    password_list.append(random.choice(letters))
for char in range(random.randint(1, len(symbols))):
    password_list.append(random.choice(symbols))
for char in range(random.randint(1, len(numbers))):
    password_list.append(random.choice(numbers))
password = ""
for char in password_list:
    password += char
print(f"Your password is {password}.")

# Differences with her code:
# 1) Because I have preexisting randomed code, on 68-70, I did not do the
# below (her method):
#   password = ""
#   for letter in range(1, nr_letters + 1)
#       random_character = random.choice(letters)
#       password += random_character
# Above can be simplified as:
#   for letter in range(1, nr_letters + 1)
#       password += = random.choice(letters)
# 2) In the hard method, she uses password_list = [] at the top to hold data
# Can keep the above code or use password_list.append(random.choice(letters))
# 3) She is able to use .shuffle() instead of .sample()
