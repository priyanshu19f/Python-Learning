"""
Q12: Take three numbers as input. Print the largest of the three without using any
built-in function.
"""


num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))
num3 = int(input("Enter number3 :"))

if num1>num2 :
    if num1 > num3 : 
        print(f"{num1} is largest")
    else : 
        print(f"{num3} is largest")
else :
    if num2 > num3 :
        print(f"{num2} is largest")
    else : 
        print(f"{num3} is largest")
