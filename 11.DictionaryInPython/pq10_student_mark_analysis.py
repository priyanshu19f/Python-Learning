"""
Q88. Student Marks Analysis

Design a dictionary where each key is a student's name and the
corresponding value is a list of their marks in 3 different subjects.
Calculate and print the total marks and average marks for each student.
"""

stu_marks = {
    "Priyanshu": [88, 67, 91],
    "Rohan": [81, 85, 90],
    "Shyam": [88, 77, 61],
    "Riya": [79, 67, 61],
}

for k, v in stu_marks.items():
    total = sum(v)
    avg = total / len(v)
    print(f"{k} : Total Marks : {total} and Average : {avg : .2f}")
