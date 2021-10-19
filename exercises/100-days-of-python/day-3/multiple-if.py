print("Welcome to the rollercoaster!")
height = int(input("What is your height in centimeters?\n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster. Congrats on  your height!")
    age = int(input("How old are you? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5. ")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7. ")
    else:
        bill = 12
        print("Adult tickets are $12. ")

    wants_photo = input(
        "Do you want a photo taken? Type Y for yes or N for no."
    )
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}.")

else:
    print("Sorry, you have to grow taller before you can ride, short king.")
