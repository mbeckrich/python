print("Welcome to the rollercoaster!")
height = int(input("What is your height in centimeters?\n"))

if height >= 120:
    print("You can ride the rollercoaster. Congrats on  your height!")
    age = int(input("How old are you?"))
    if age < 12:
        print("Please pay $5 for your ticket.")
    elif age <= 18:
        print("Please pay $7 for your ticket.")
    else:
        print("Please pay $12 for your ticket.")
else:
    print("Sorry, you have to grow taller before you can ride, short king.")
