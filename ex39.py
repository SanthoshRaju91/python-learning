things = ["a", "b", "c", "d"]
print(things[1])
things[1] = "z"
print(things[1])

print(things)

stuff = {
    "name": "Zed",
    "age": 39,
    "height": 6 * 12 + 2
}
print(stuff["name"])
print(stuff["age"])
print(stuff["height"])

stuff["city"] = "SF"
print(stuff["city"])

stuff[1] = "Wow"
stuff[2] = "Neato"

print(stuff[1])
print(stuff[2])

del stuff["city"]
del stuff[1]
del stuff[2]

print(stuff)


states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}

cities = {
    "CA": "San Francisco",
    "MI": "Detroit",
    "FL": "Jacksonville"
}

cities["NY"] = "New York"
cities["OR"] = "Portland"

print("-" * 10)
print("NY State has: ", cities["NY"])
print("OR State has: ", cities["OR"])

print("-" * 10)
print("Michigan's abbreviation is: ", states["Michigan"])
print("Florida's abbreviation is: ", states["Florida"])

print("-" * 10)
print("Michigan has: ", cities[states["Michigan"]])
print("Florida has: ", cities[states["Florida"]])

print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print("-" * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

# safely get a abbreviation by state that might not be there
print("-" * 10)
state = states.get("Texas")

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get("TX", "Does Not Exist")
print(f"The city for the state 'TX' is: {city}")
