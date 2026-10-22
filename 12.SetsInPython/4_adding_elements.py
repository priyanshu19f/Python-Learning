# Use add() for single elements, and
# update() for multiple elements from an iterable.

fruits = {"apple", "banana"}
print(fruits)

fruits.add("kiwi")
print(fruits)

# fruits.add("pineapple")
# fruits.add("grapes")
# fruits.add("guvava")
fruits.update(["pineapple", "grapes", "guvava"])
print(fruits)
