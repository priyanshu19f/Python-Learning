"""
Question 64

Given a list of numbers (which may contain duplicates), write a
Python script that takes an integer as input from the user and
removes all occurrences of that integer from the list.
""" 

def remove_all_occurence(lst, x):
    new_list = []
    for item in lst:
        if item != x:
            new_list.append(item)
    return new_list

my_list = [10,10,10,10, 20, 10, 30, 20, 10, 40]
x = int(input("Enter a number : "))
print(remove_all_occurence(my_list, x))