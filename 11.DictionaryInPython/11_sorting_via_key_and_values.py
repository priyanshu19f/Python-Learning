marks = {
    "maths": 99,
    "science": 92,
    "english": 80,
    "hindi": 78,
    "computer": 82,
}

print(sorted(marks.items()))  # sorted by default sort by first index in tuples

ans = dict(sorted(marks.items(), key=lambda x: x[1]))
print(ans)


my_list = [
    ("hindi", 78),
    ("english", 80),
    ("computer", 82),
    ("science", 92),
    ("maths", 99),
]
print(dict(my_list))
# automatically 0th index becomes key and 1st index becomes value
