Procedural programming up until now. Creates longer spaghetti code. As programming got more complicated, object-oriented programming
came into being. OOP separates projects into modules, which can be reusable.

Restaurant example: Owning a restaurant as a manager vs. doing every role at the restaurant yourself. Employees are the modules that specialize in one thing.

Waiter module:

Has/attributes (basically a variable):
is_holding_plate = True
tables_responsible = [4, 5, 6]

Does/methods (function a particular modeled object can do):
def take_order(table, order):
def take_payment(amount):
"What the waiter does"

The waiter is a 'class' and the individual waiter is an 'object.'

Object = Class (Pascal case):
car = CarBlueprint()
from car object, get speed attribute:
car.speed <- object.attribute

Function tied to an object is a method
car.stop() <- object.method
