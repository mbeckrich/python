# Write your code below this line 👇

temp_list = []


def prime_checker(number):
    for i in range(2, number + 1):
        temp_list.append(number % i)
    if temp_list.count(0) == 1:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

# Differences in her code:
# 1) for i in range(2, number):
# if number % i == 0
