"""
Question 57: Check if a List is Sorted

Write a program that takes a list of numbers and, using a loop, 
determines whether it is sorted in ascending order. Print True if it is sorted, and False otherwise.

Do not use built-in sort or sorted() functions for checking.
"""



def check_sorted(lst):
    n = len(lst)
    if n == 0:
        return True
        return
    for k in range(1,n):
        if lst[k] < lst[k-1]:
            return False
    return True


lst = [10, 20, 30, 40]
# lst = [10, 20, 30, 40, 12]
# lst = [ ]

print(check_sorted(lst))
