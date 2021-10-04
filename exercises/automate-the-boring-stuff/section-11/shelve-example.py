import shelve

# Returns a shelf file object, treats file as dictionary
shelf_file = shelve.open("my_data")
shelf_file["Cats"] = ["Zophie", "Pooka", "Simon", "Fat tail", "Cleo"]

# Treats "Cats" as key
print(list(shelf_file.keys()))

# Shows "Cats" values
print(list(shelf_file.values()))

shelf_file.close()
