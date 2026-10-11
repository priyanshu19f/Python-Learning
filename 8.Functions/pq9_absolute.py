"""
Q43. Write a function called absolute_value that takes a number and returns
its absolute value without using the built-in abs() function.
"""

def absolute_value(n):
    if n>=0 :
        return n
    else :
        return -n

print(absolute_value(67))
print(absolute_value(0))
print(absolute_value(-25))