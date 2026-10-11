"""
Q4: A student scored marks in 3 subjects. Take all three as input,
calculate the total and average, and print both using an f-string.
"""

n1 = int(input("Enter marks in subject 1 : "))
n2 = int(input("Enter marks in subject 2 : "))
n3 = int(input("Enter marks in subject 3 : "))

total = n1+n2+n3
avg = total/3

print(f"Total marks : {total} , average : {avg:.2f}")