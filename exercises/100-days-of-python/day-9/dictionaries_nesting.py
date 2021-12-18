# Lists and dicts can be nested in dicts
# e.g.
# {
# key: []
# key2: {}
# }

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Can't assign multiple values to key,
# so no France = cities, I've, been, to
# Use list instead
travel_log = {"France": ["Paris", "Lille", "Dijon"]}

# Can also nest lists in lists, but less useful

# Dicts in dicts
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "United States": {
        "cities_visited": ["Seattle", "Denver", "Chicago"],
        "total_trips": 20,
    },
}

# Dicts in lists

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]
