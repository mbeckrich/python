# ###########DEBUGGING#####################

# Describe Problem
# range needs to go to 21
# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")


# my_function()

# Reproduce the Bug
# set to 0,5 instead of 1,6
# from random import randint

# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# 1994 is missed because there is no >= or <=
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year >= 1994:
#     print("You are a Gen Z.")

# # Fix the Errors
# no f string
# change input() to int(input())
# add else: to let user know they cannot drive yet
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")
# else:
#     print("You cannot drive yet.")

# #Print is Your Friend
# remove extra = sign at word_per_page
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# add b_list.append to loop
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
