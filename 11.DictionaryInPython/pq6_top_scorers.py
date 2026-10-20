"""
Q84: Top Scorers

Populate a dictionary with six student names and their corresponding
marks. Loop through it and print the names of all students who achieved
a score above 75.
"""

marks = {
    "Priyanshu": 85,
    "Rohan": 76,
    "Shyam": 68,
    "Pragya": 92,
    "Suraj": 70,
    "Sunil": 91,
}

for stu, mark in marks.items():
    if mark > 75:
        print(stu)
