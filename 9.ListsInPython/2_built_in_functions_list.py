marks = [23, 35, 93, 85, 65, 39]

# To get the length of the list 
n = len(marks)
print(f"Length of the list : {n}")

# max -> to get maximum
maxi = max(marks)
print(f"Maximum marks : {maxi}")

# min -> to get minimum
mini = min(marks)
print(f"Minimum marks : {mini}")

# sum -> to get total sum
totalMarks = sum(marks)
print(f"Total marks : {totalMarks}")


# to sort using sorted()  -> it will always return a new list assecending order
new_list = sorted(marks)
print(f"new sorted list : {new_list}")

new_list2 = sorted(marks, reverse=True)
print(f"new sorted list descending order: {new_list2}")

print(f"Original list remains the same : {marks}")