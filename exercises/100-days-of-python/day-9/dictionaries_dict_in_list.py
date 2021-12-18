travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
    },
]


def add_new_country(country, visits, cities):
    add_new_country = {"country": country, "visits": visits, "cities": cities}
    travel_log.append(add_new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# Differences in her code:
# add_new_country(country_visited, times_visited, cities_visited):
#     new_country={}
#     new_country["country"] = country_visited
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited
