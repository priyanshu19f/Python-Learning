"""
Q46. Write a function fizzbuzz(n) that takes a single number and prints "Fizz"
if it's divisible by 3, "Buzz" if it's divisible by 5, "FizzBuzz" if it's divisible
by both, otherwise print the number itself.
"""


def fizzbuzz():
    n = int(input("Enter a number : "))
    if(n%3==0 and n%5==0):
        print("FizzBuzz")
    elif n%3==0 :
        print("Fizz")
    elif n%5==0 :
        print("Buzz")
    else:
        print("Not divisible by 3 and 5 both")

fizzbuzz()