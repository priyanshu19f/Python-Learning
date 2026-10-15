"""
Question 73

Given a 4x4 matrix, print only the border elements and replace the
inner elements with an asterisk (*).
"""

# Input:
# 1   2  3 4
# 5  6  7 8
# 9 10 11 12
# 13 14 15 16


# Expected Output:
# 1  2  3  4
# 5 *   *    8
# 9 *   *   12
# 13 14 15 16


matrix = [
    [1, 2, 3, 5],
    [9, 1, 8, 7],
    [4, 8, 3, 6],
    [5, 8, 2, 4],
]
rows = len(matrix)
column = len(matrix[0])


for i in range(0, rows):
    for j in range(0, column):
        if i == 0 or i == rows - 1 or j == 0 or j == column - 1:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()
