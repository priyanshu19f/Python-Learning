"""
Question 68
Create a 3x3 matrix (a nested list) and then use nested loops to
calculate and print the sum of all its elements.

"""

matrix = [
    [2, 5, 5],
    [9, 1, 8],
    [4, 8, 3],
]

total = 0
for i in range(0, 3):
    for j in range(0, 3):
        total += matrix[i][j]

print(f"Total : {total}")
