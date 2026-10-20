"""
Q79: Student Profile (HW)

Create a dictionary for a student, including keys like name, age, city, and
marks (as a list of scores). Print each piece of information using its key.
"""

student = {
    "name": "Priyanshu",
    "age": 22,
    "city": "Lucknow",
    "marks": [88, 82, 92, 84, 74],
}

for k in student:
    print(f"{k} : {student[k]}")
