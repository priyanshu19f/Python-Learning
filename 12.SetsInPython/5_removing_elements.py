# Python offers methods like
# remove(), discard(), pop(), and clear() to manage set elements.

fruits = {"grapes", "kiwi", "apple", "guvava", "banana", "pineapple"}
print(fruits)

# 1 remove()
fruits.remove("kiwi")
# fruits.remove("kiwiiii")        KeyError: 'kiwiiii'
print(fruits)


# 2 discard()
fruits.discard("apple")
fruits.discard("appleee")  # no error
print(fruits)


# 3 pop() -> random delete
removed = fruits.pop()
print(f"{fruits} , removed element = {removed}")


# 4 clear -> empty the set
fruits.clear()
print(fruits)
