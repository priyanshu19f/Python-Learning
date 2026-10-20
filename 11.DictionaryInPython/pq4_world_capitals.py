"""
Q82: World Capitals (HW)

Create a dictionary mapping five countries to their capital cities. Iterate through this
dictionary using the items () method and print each pair in the format: Country ->
Capital.
"""

world_capital = {
    "India": "New Delhi",
    "Canada": "Ottawa",
    "UK": "London",
    "Australia": "Canberra",
    "USA": "Washington DC",
}

for country, capital in world_capital.items():
    print(f"{country} -> {capital}")
