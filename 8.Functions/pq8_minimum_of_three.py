"""
Q42. Write a function called min_of_three that takes three numbers and returns
the smallest without using any built-in function.
"""

def min_of_three(a, b, c):
    if a>b:
        if b<c:
            return b
        else :
            return c
    else :  # a<b
        if a<c:
            return a
        else :
            return c

ans = min_of_three(5, 8, 3)
print(ans)