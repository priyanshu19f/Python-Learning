"""
Q60. Given two lists, merge them into a
single new list without modifying the
originals.
"""

def merge(lst1, lst2):
    # n = len(lst1) + len(lst2)
    new_list = lst1 + lst2
    # for i in range(0,n):


    return new_list
        

lst1 = [10, 20, 30, 40]
lst2 = [1, 2, 3, 4]
print(merge(lst1, lst2))