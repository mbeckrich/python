from prettytable import PrettyTable

pokemon_table = PrettyTable()


pokemon_table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
pokemon_table.add_column("Pokemon Type", ["Electric", "Water", "Fire"])
pokemon_table.align = "l"
print(pokemon_table)
