# 3 by 3 matrix

matrix = [
    [2, 5, 5],
    [9, 1, 8],
    [4, 8, 3],
]

print(matrix)
print(type(matrix))

print(matrix[0])
print(matrix[1])
print(matrix[1][1])

# printing using for loop
for i in range(0, 3):
    for j in range(0, 3):
        print(matrix[i][j], end=" ")
    print()
