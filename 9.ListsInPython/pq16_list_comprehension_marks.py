"""
Q67. Given a list of marks, use list comprehension to create a new list that contains
only the marks that are above 75.
"""

marks = [41, 73, 79, 83,43, 47, 53, 59, 61, 67, 71, 89, 97] 

marks_above_75 = [i for i in marks if i>75 ]
print(marks_above_75)