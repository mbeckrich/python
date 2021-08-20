# eggs variable isn't recognized when`spam()` function is called
# this is an example of local variable being used in global scope

# def spam():
#     eggs = 99

# spam()
# print(eggs)

# local scope is created for spam() function. in bacon(), local scope is created as well.
# eggs in spam() and eggs in bacon() are two separate variables. when spam() is called,
# it takes the spam function's argument and its print(eggs) -- two local scope items.


def spam():
    eggs = 99
    bacon()
    print(eggs)


def bacon():
    ham = 101
    eggs = 0


spam()

# spam is global and `eggs = 42` is global. python sees no local `eggs` variable defined
# in `print(eggs)`, so it is smart enough to look for a global variable of that name.


def spam():
    print(eggs)


eggs = 42
spam()

# if there is an assignment statement inside a function, python considers it a local variable.
# otherwise, it is a global variable. python prefers the local variable.


def spam():
    eggs = 99
    print(eggs)


eggs = 42
spam()


def spam():
    eggs = "Hello"
    print(eggs)


eggs = 42
spam()  # spam will call `eggs = "Hello"` and print(eggs), which is "Hello"
print(
    eggs
)  # when `eggs` is global, `print(eggs)` calls the `eggs` global variable rather than the spam() function's eggs
