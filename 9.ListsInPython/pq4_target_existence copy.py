"""
Question 54: Check for Target Existence

Write a program that takes a list and a target number. Use a loop 
to determine if the target number exists in the list. Do not use the in operator.
"""

def check_target(lst, target):
    for num in lst :
        if num==target:
            return True
    return False

        
my_lst = [10,20, 30, 40, 50]
print(check_target(my_lst, 18))
print(check_target(my_lst, 20))
    