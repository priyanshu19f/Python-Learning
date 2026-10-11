"""
Take numbers as input from the user one by one. Skip negative
numbers and keep adding the positive ones. Stop when the user
enters 0 and print the total. (Uses both continue and break.)
"""

sum = 0
while True : 
    n = int(input("Enter a number(0 to stop) : "))

    if n==0: 
        break
    if n<0:
        continue
    
    sum += n

print(f"Sum of all positive numbers : {sum}")