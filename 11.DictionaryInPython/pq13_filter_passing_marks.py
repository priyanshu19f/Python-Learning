"""
Q91. Filter Passing Marks
Given an existing dictionary of subjects and their respective marks, use
dictionary comprehension to generate a new dictionary that includes
only the subjects where the student scored 40 or more (i.e., passed).
"""

marks = {
    "english": 85,
    "hindi": 78,
    "maths": 30,
    "computer": 32,
    "science": 95,
    "social science": 88,
}

pass_sub = {sub: mark for sub, mark in marks.items() if mark >= 40}
print(pass_sub)
