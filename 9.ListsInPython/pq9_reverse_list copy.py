"""
Q59. Reverse a list without using the
. reverse() method or list slicing
([ ::- 1]).
"""

def reverse_list(lst):
    reverse = []
    for i in range(len(lst)-1,-1,-1):
        reverse.append(lst[i])
    return reverse

nums = [4, 7, 3, 8, 1, 1, 2, 10, 9, 6, 9, 1, 1, 1]
print(reverse_list(nums)) 
print(nums)