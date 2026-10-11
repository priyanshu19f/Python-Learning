"""
        1
      12
    123
  1234
12345
"""

for i in range(1,6):

    for k in range(4,i-1,-1):
        print(" ",end=" ")

    for j in range(1,i+1):
        print(j,end=" ")

    print()