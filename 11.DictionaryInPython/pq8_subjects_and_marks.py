"""
Q86. Subjects and Marks

Create a dictionary of 6 subjects and their respective marks. Print the
subject with the highest marks and the one with the lowest, using max ()
and min() functions alongside a lambda expression.
"""

marks = {
    "english": 85,
    "hindi": 78,
    "maths": 90,
    "computer": 92,
    "science": 95,
    "social science": 88,
}

maxi = max(marks.items(), key=lambda x: x[1])
mini = min(marks.items(), key=lambda x: x[1])
print(f"maximum: {maxi}")
print(f"minimum: {mini}")
