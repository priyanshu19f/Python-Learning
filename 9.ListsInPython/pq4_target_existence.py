"""
Question 54: Check for Target Existence

Write a program that takes a list and a target number. Use a loop 
to determine if the target number exists in the list. Do not use the in operator.
"""
my_lst = [10,20, 30, 40, 50]


def check_target(lst):
    target = int(input("Enter target : "))
    for num in my_lst :
        if num==target:
            print(f"{target} exists in list")
            return
        
    print(f"{target} does not exists in list")
    
check_target(my_lst)
    