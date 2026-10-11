"""
Q28.
5
54
543
5432
54321
5432
543
54
5
"""
# n = int(input("Enter a number : "))

for i in range(5,0, -1):
    for j in range(5, i-1, -1):
        print(j,end=" ")
    print()

for i in range(2,6):
    for j in range(5, i-1, -1):
        print(j,end=" ")
    print()