marks = {
    "maths": 99,
    "science": 92,
    "english": 80,
    "hindi": 78,
    "computer": 82,
}

print(marks.values())

total = 0
for mark in marks.values():
    print(mark)
    total += mark

print(total)
