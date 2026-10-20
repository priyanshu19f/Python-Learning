# create a dictionary that consist of num 1 to 10 and their squares

squares = {}
for i in range(1, 11):
    squares[i] = i * i
print(squares)

# using dict comprehsion -> in one line
squares1 = {i: i * i for i in range(1, 11)}
print(squares1)


# With a condition
marks = {"math": 85, "science": 92, "english": 60, "hindi": 45}

# Keep only subjects where marks > 80
# top_sub = {sub: marks[sub] for sub in marks if marks[sub] > 80}
top_sub = {sub: m for sub, m in marks.items() if m > 80}
print(top_sub)

# double each mark
double = {sub: m * 2 for sub, m in marks.items()}
print(double)


# creating a dict from two lists
subjects = ["english", "hindi", "maths"]
scores = [93, 92, 99]

result = {s: sc for s, sc in zip(subjects, scores)}
print(result)
