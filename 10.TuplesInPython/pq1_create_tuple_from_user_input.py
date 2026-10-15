"""
Q77: Take 5 numbers as input from the user, store them in a
tuple, and print the tuple along with its minimum and maximum.
"""

n1 = int(input(f"Enter number 1 : "))
n2 = int(input(f"Enter number 2 : "))
n3 = int(input(f"Enter number 3 : "))
n4 = int(input(f"Enter number 4 : "))
n5 = int(input(f"Enter number 5 : "))

my_tuple = n1, n2, n3, n4, n5
print(f"tuple : {my_tuple}, max : {max(my_tuple)} , min : {min(my_tuple)}")
