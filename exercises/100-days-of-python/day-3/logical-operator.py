# and: both A and B == True
# or: A or B == True
# not: if A == True, A == False & vice versa

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
    elif age < 45 and age > 55:
        bill = 12
        print("Adult tickets are $12. ")
    else:
        bill = 0
        print("Sorry about the midlife crisis. Your ride is free.")

    wants_photo = input(
        "Do you want a photo taken? Type Y for yes or N for no."
    )
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}.")

else:
    print("Sorry, you have to grow taller before you can ride, short king.")

# Differences with her code:
# 1) She uses elif at line 18 to offer free ticket:
# elif age >= 45 and age <= 55
# 2) She does not do bill = 0 for midlife crisis
