# def greet_with(name, location):
#     print(f"Hello, {name}.")
#     print(f"What is it like in {location}?")


# greet_with("Marshall", "Colorado")  # positional argument
# # positional argument is default way of calling functions

# # keyword arguments can be added to avoid this
# # greet_with(a=Marshall, b=Colorado)


def greet_with(name, location):
    print(f"Hello, {name}.")
    print(f"What is it like in {location}?")


greet_with(name="Marshall", location="Colorado")
# less error prone, but longer. Use best judgment.
