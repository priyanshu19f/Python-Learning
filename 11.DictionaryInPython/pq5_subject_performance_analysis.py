"""
Q83: Subject Performance Analysis

Given a dictionary of marks for different subjects, loop over its values () to calculate
and print the total marks and the average mark obtained.
"""

marks = {
    "maths": 99,
    "science": 92,
    "english": 80,
    "hindi": 78,
    "computer": 82,
}

total_marks = 0
total_subjects = 0
for mark in marks.values():
    total_marks += mark
    total_subjects += 1

avg = total_marks / total_subjects

print(f"Total Marks : {total_marks}")
print(f"Average : {avg}")
