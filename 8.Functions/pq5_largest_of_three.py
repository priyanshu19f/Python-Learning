"""
Q39. Write a function called find_max that takes three numbers as
parameters and prints the largest one.
"""

def find_max(a,b,c):
    if a>b:
        if a>c:
            print(f"{a} is largest")
        else :
            print(f"{c} is largest")

    else:   # a<b
        if b>c:
            print(f"{b} is largest")
        else :
            print(f"{c} is largest")

find_max(23, 45, 10)