# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum


# print(add(3, 4, 5))


# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)


# calculate(2, add=3, multiply=5)


# class Car:
#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")
# kwargs.get("make") vs. kwargs["make"]
# .get() prevents error if no keyword argument

# my_car = Car(make="Honda", model="Civic")
# print(my_car.model)
