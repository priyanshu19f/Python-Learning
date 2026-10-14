"""
Question 65

Write a Python script that iterates through a list of integers and
replaces every negative number found in the list with the value 0.
"""

def replace_neg(lst):
    for i in range(0,len(lst)) :
        if lst[i]<0: 
            lst.remove(lst[i])
            lst.insert(i,0)
    return lst

numbers = [5,-3,8,-1,0, -10, 12]
print(replace_neg(numbers))