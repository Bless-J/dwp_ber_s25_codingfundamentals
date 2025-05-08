european_cities_info = {}

european_cities = [
    ("Istanbul", [15460000, "Kebab", "Hagia Sophia"]),
    ("Moscow", [12678079, "Borscht", "Red Square"]),
    ("London", [8982000, "Fish and Chips", "Big Ben"]),
    ("St. Petersburg", [5383890, "Blini", "Hermitage Museum"]),
    ("Berlin", [3669491, "Currywurst", "Brandenburg Gate"]),
    ("Madrid", [3348536, "Paella", "Royal Palace of Madrid"]),
    ("Kiev", [2884000, "Borscht", "Saint Sophia's Cathedral"]),
    ("Paris", [2140526, "Croissant", "Eiffel Tower"])
]

for city, info in european_cities:
    european_cities_info[city] = info

print("Main Dictionary:")
for city, info in european_cities_info.items():
    print(f"{city} --> {info}")
sorted_cities_info = dict(sorted(european_cities_info.items()))
print("\nSorted Dictionary:")
for city, info in sorted_cities_info.items():
    print(f"{city} --> {info}")

print("\nBerlin Info:", european_cities_info.get("Berlin", "Not Found"))

print("Type of London Info:", type(european_cities_info.get("London", "Not Found")))

print("Barcelona Info:", european_cities_info.get("Barcelona", "Not Found"))

european_cities_info["Rome"] = [2870500, "Pasta", "Colosseum"]

european_cities_info.pop("Madrid", None)


if "Warsaw" in european_cities_info:
    print("Warsaw is in the dictionary.")
else:
    print("Warsaw is not in the dictionary.")

dishes = ["Pizza", "Sauerkraut", "Paella", "Hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]

food_dict = dict(zip(countries, dishes))
print("\nCountry to Dish Dictionary:", food_dict) 