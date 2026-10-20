marks = {
    "science": 88,
    "maths": 99,
    "computer": 87,
    "history": 82,
    1: 100,
}

print(marks["maths"])
print(marks[1])

# print(marks["abc"])             # KeyError: 'abc'
print(marks.get("maths"))
print(marks.get("mathssssss"))  # None
print(marks.get("mathssssss", "key not exist"))  # None


subject = "history"
subject = "historyy"
print(marks.get(subject, "subject not found"))
