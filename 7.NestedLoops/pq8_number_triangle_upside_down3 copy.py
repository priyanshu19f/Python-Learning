"""
Q26.
54321
4321
321
2 1
1
"""
# n = int(input("Enter a number : "))

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()