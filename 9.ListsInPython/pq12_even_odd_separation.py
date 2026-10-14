"""
Question 62

Separate a list of integers into two distinct lists: one
containing all the even numbers and the other
containing all the odd numbers.
"""


lst = [10, 20, 30, 40, 1, 2, 3, 4]

even = []
odd = []

for i in lst:
    if i % 2 == 0:
        even.append(i)
    else : 
        odd.append(i)

print(f"Even : {even}")
print(f"Odd : {odd}")