"""
Question 72

Given a 3x3 matrix, print only the anti-diagonal (top-right to bottom-left)
elements and replace everything else with an asterisk (*).
"""

# Input:
# 123
# 456
# 789

# Expected Output:
# * * 3
# * 5 *
# 7 * *


matrix = [
    [2, 5, 5],
    [9, 1, 8],
    [4, 8, 3],
]
rows = len(matrix)
column = len(matrix[0])

for i in range(0, rows):
    for j in range(0, column):
        if j + i != rows - 1:
            matrix[i][j] = "*"

for i in range(0, rows):
    for j in range(0, column):
        print(matrix[i][j], end=" ")
    print()
