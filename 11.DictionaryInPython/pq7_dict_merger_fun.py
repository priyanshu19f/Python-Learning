"""
Q85: Dictionary Merge Function

Write a Python function named merge_dicts(d1, d2) that accepts two
dictionaries (d1 and d2) as arguments and returns a new dictionary
formed by merging them using the update() method. Ensure d1 remains
unchanged.
"""


def merge_dicts(d1, d2):
    new_dict = {}
    new_dict.update(d1)
    new_dict.update(d2)
    return new_dict


marks = {
    "Priyanshu": 85,
    "Rohan": 76,
    "Shyam": 68,
    "Pragya": 92,
    "Suraj": 70,
    "Sunil": 91,
}

product = {
    "laptop": 50000,
    "phone": 20000,
    "tablet": 30000,
    "headphone": 4500,
}
print(merge_dicts(marks, product))
