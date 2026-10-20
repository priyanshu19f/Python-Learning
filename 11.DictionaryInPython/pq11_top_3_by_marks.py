"""
Q89. Top 3 Subjects by Marks
Given a dictionary of subjects and their marks, sort it by marks in descending
order. Then, print only the top 3 subjects with the highest marks.
"""

marks = {
    "english": 85,
    "hindi": 78,
    "maths": 90,
    "computer": 92,
    "science": 95,
    "social science": 88,
}

marks = dict(sorted(marks.items(), key=lambda x: x[1], reverse=True))
print(marks)

print()
print("top 3 subjects with the highest marks")
i = 1
for k, v in marks.items():
    if i == 4:
        break
    print(f"{k} : {v}")
    i += 1
