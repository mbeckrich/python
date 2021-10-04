# Adds your own message to an error message

"""
*****************
*               *
*               *
*               *
*               *
*****************

"""


def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception(
            "Symbol needs to be a string of length one."
        )  # This gives an error if we try to use a len > 1 in the function call
    if (width < 2) or (height < 2):
        raise Exception(
            "Width or Height must be greater or equal to 2."
        )  # This gives an error message if width or height exceeds 1 in function call.
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)

    print(symbol * width)


box_print("*", 5, 15)
