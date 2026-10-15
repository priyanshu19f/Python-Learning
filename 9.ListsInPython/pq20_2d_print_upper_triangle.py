"""
Given a 3x3 matrix, print its upper triangle. Replace all elements in the
upper triangle (below the main diagonal) with an asterisk (*).
"""

# Input:
# 123
# 456
# 789

# Expected Output:
# 1 2 3
# * 5 6
# * * 9


matrix = [
    [2, 5, 5],
    [9, 1, 8],
    [4, 8, 3],
]
rows = len(matrix)
column = len(matrix[0])

for i in range(0, rows):
    for j in range(0, column):
        if j < i:
            matrix[i][j] = "*"

for i in range(0, rows):
    for j in range(0, column):
        print(matrix[i][j], end=" ")
    print()
