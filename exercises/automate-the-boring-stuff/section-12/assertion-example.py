market_2nd = {"ns": "green", "ew": "red"}


def switch_lights(intersection):
    for key in intersection.keys():
        if intersection[key] == "green":
            intersection[key] = "yellow"
        elif intersection[key] == "yellow":
            intersection[key] = "red"
        elif intersection[key] == "red":
            intersection[key] = "green"
    assert "red" in intersection.values(), "Neither light is red!" + str(intersection)


# Assertion statement holds that code always holds true. If it fails test, will return
# a more detailed message you tell it to give.
# Assertion errors are for programmer errors, not user errors. Use a raise exception
# error for user errors.
# Assertions are "sanity checks," never expect them to be raised.

print(market_2nd)
switch_lights(market_2nd)
print(market_2nd)
