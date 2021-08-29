eggs = {"name": "Zophie", "species": "cat", "age": 8}

for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

# .items() returns two item tuples, k, v stores them as variables
for k, v in eggs.items():
    print(k, v)

# with just i, entire tuple is printed. e.g. ('name', 'Zophie')
for i in eggs.items():
    print(i)
