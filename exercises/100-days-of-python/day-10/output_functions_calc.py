def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

num1 = int(input("What is the first number?: "))
operation_symbol = input("Pick an operation from the line above: ")

num2 = int(input("What is the second number?: "))

for symbol in operations:
    print(symbol)


for choice in operation_symbol:
    answer = operations[choice](num1, num2)


print(f"{num1} {operation_symbol} {num2} = {answer}")

# Her code:
# No for loop, just does:
# calculation_function = operations[operation_symbol]
# answer = calculation_function(num1, num2)
