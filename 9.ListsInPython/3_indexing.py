lst = ["Priyanshu", "Archit","Suresh", 55, 46.335, True, 3738, 2839]

print(lst[0])
print(lst[1])

print(lst[5])
print(lst[-1])

print(lst[-3])

# print(lst[99])   -> IndexError: list index out of range


n = len(lst)
print(f"last element of list : {lst[n-1]}")