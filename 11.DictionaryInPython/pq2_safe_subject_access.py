"""
Q80: Safe Subject Access (HW)

Define a dictionary with five subjects and their respective marks. Utilize the
get() method to try accessing a subject that is not in the dictionary, ensuring
it prints "Not Available" as a default.
"""

marks = {
    "maths": 99,
    "science": 92,
    "english": 80,
    "hindi": 78,
    "computer": 82,
}

subject = input("Enter subject : ").lower()

mark = marks.get(subject)

if mark is None:
    print("Not Available")
else:
    print(f"Marks in subject {subject} = {mark}")
