"""
Q59. Reverse a list without using the
. reverse() method or list slicing
([ ::- 1]).
"""

def reverse_list(lst):
    i = 0
    j = len(lst) - 1
    while(i<j):
        lst[i] = lst[i] + lst[j]
        lst[j] = lst[i] - lst[j]
        lst[i] = lst[i] - lst[j]
        i += 1
        j -= 1
    return lst

nums = [4, 7, 3, 8, 1, 1, 2, 10, 9, 6, 9, 1, 1, 1]
print(reverse_list(nums)) 
print(nums)