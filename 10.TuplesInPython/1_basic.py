my_tuple = (1, 2, 4, "Priyanshu")

print(my_tuple)
print(type(my_tuple))

# Immutable
# my_tuple[1] = 0         TypeError: 'tuple' object does not support item assignment

print(f"Count : {my_tuple.count(1)}")
print(f"index : {my_tuple.index("Priyanshu")}")
