# input function:
# def my_function(something):
#     do this with something
#     then this
#     finally this

# my_function(123)

# output function:
# def my_function():
#     result = 3 * 2
#     return result

# my_function() is replaced with result
# output = my_function()

# changes names into titlecase
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


formatted_string = format_name("IrA", "pumpKIN")
print(formatted_string)  # or print(format_name("IrA", "pumpKIN))
put = len("Ira")
