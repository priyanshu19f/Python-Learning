"""
Question 53: Find the Largest Element
Given a list of numbers, write Python code using a loop to find 
and print the largest element. Do not use the built-in max() function.
"""

lst = [3,1,4,15, 1,5,9,2,6]
largest = lst[0]

for num in lst :
    if num > largest : 
        largest = num

print(f"Largest num : {largest}")