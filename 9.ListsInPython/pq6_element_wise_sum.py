"""
Question 56: Element-wise Sum of Two Lists

Given two lists of the same length, write Python code using a loop 
to create a new list where each element is the sum of the corresponding elements from both original lists.
"""

def sum_of_two_list(lst1, lst2):
    n = len(lst2)
    ans_lst = []
    for i in range(0,n):
        total  = lst1[i] + lst2[i]
        ans_lst.append(total)
    return ans_lst


lst1 = [10, 20, 30, 40]
lst2 = [1, 2, 3, 4]

print(sum_of_two_list(lst1, lst2))