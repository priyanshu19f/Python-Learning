"""
Q18. Ask a number from the user, print the multiplication table upto 10.
"""

n = int(input("Enter a number : "))

i = 1
j = n
while i<=10:
    print(f"{n} * {i} = {j}")
    j += n
    i += 1
    
