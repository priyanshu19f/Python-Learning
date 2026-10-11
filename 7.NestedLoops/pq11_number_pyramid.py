"""
Q29.
        1
      123
    12345
  1234567
123456789
  1234567
    12345
      123
        1
"""
# n = int(input("Enter a number : "))
n = 5
for i in range(1,n+1):
    for k in range(1,n-i+1):
        print(" ", end=" ")

    for j in range(1, 2*i):
        print(j, end=" ")

    print()

for i in range(n-1,0,-1):
    for j in range(1,n-i+1):
        print(" ",end=" ")

    for k in range(1,2*i):
        print(k, end=" ")
    print()