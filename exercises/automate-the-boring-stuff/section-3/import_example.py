# in terminal
import random  # imports random number module

# `random.` tells python to look inside the `random` module,
# randint only exists inside the `random` module
random.randint(1, 10)  # picks random int() between 1-10

# can import multiple modules at the same time like below
import random, sys, os, math

# imports random module + everything in it
from random import *

# this method allows you to use `randint` without `random.` first,
# but `import` is better because the full name makes for more readable code.
# `random.randint` vs `randit`
randint(1, 10)

# ends script
import sys

sys.exit()
