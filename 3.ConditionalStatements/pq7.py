"""
Q13: Take a number as input. Using the ternary operator, print "Even" or "Odd" in a single line.
"""

num = int(input("Enter a number :"))
status = "Even" if num%2==0 else "Odd"
print(status)