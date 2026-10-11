"""
Q8: Take two numbers as input. Print the greater of the two. If they are
equal, print "Both are equal."
"""

num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))

if num1 == num2:
    print("Both are equal")
elif num1 < num2:
    print(f"{num2} is greater")
else : 
    print(f"{num1} is greater")