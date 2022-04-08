import pandas

nato_alphabet = pandas.read_csv(
    "./day-26/NATO-alphabet-start/nato_phonetic_alphabet.csv"
)

alphadict = {
    nato_alphabet.letter: nato_alphabet.code
    for (nato_alphabet, nato_alphabet) in nato_alphabet.iterrows()
}

user_word = input("Type in a word to receive the NATO alphabet form: ").upper()

# Returns alphabetized result, doesn't work
# result = [
#     code for letters, code in alphadict.items() if letters in user_word.upper()
# ]
# Her answer:
output_list = [alphadict[letter] for letter in user_word]

print(f"Your word in the NATO alphabet is {output_list}.")
