marks = {
    "maths": 99,
    "science": 92,
    "english": 80,
    "hindi": 78,
    "computer": 82,
}

print(marks.keys())

total = 0
for sub in marks:
    # print(sub, marks[k])
    print(f"subject : {sub} and marks : {marks[sub]}")
    total += marks[sub]

print(f"total marks = {total}")
