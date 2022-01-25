def likes(names):
    if len(names) == 0:
        return print("No one likes this.")
    elif len(names) == 1:
        return print(f"{names[0]} has liked this.")
    elif len(names) == 2:
        return print(f"{names[0]} and {names[1]} have liked this.")
    elif len(names) == 3:
        return print(
            f"{names[0]}, {names[1]} and {names[2]} have liked this.")
    elif len(names) > 3:
        return print(
            f"{names[0]}, {names[1]} and {len(names) -2} others have liked this.")


likes(["Tenley", "Ira"])
