# 3 int as parameter , print total

def addition(a, b, c):
    sum = a + b + c
    print(f"Total : {sum}")

addition(44, 55,23)


# ask name, age, gender and print

def greet(name, age, gender):
    print(f"Hey! {name}, you are {age} years old and your gender is {gender}")


greet("Priyanshu", 22 , "Male")

n = input("Enter your name : ")
a = int(input("Enter your age : "))
g = input("Enter your gender : ")

greet(n, a, g)