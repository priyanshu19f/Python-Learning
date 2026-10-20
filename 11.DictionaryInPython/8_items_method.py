marks = {
    "maths": 99,
    "science": 92,
    "english": 80,
    "hindi": 78,
    "computer": 82,
}

print(marks.items())

for details in marks.items():
    print(details)
    print(f"subject : {details[0]} and marks : {details[1]}")


# unpacking
for sub, mark in marks.items():
    print(f"subject = {sub}, marks = {mark}")
