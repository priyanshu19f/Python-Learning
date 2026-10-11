"""
Q6: Take two numbers as input. Without using *, calculate and print their product
using += in a way that adds the first number to itself the
second number of times. (Think carefully.)
"""

n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))

# (a + b)² = a² + 2ab + b², from here ->  a × b = ((a + b)² − a² − b²) / 2

product = n1
product += n2          # n1 + n2
product **= 2          # (n1 + n2) ** 2
product -= n1 ** 2     # minus n1 ka square
product -= n2 ** 2     # minus n2 ka square
product //= 2          # 2ab / 2 = ab

print(product)
