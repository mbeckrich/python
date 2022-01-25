def disemvowel(string_):
    return "".join([i for i in string_ if i.casefold() not in "aeiou"])


disemvowel("This website is for losers LOL!")
