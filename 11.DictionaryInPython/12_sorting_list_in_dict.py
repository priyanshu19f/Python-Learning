marks = {
    "akshy": [43, 12, 98, 10, 22],
    "priya": [76, 55, 34, 89, 61],
    "rahul": [20, 45, 67, 30],
    "sneha": [91, 73, 50],
    "karan": [38, 82, 47, 95, 29],
}


# sorted on basis of last index
ans = dict(sorted(marks.items(), key=lambda x: x[1][-1]))
print(ans)


# sorting on basis of total
print("sorting on basis of total")
ans1 = dict(sorted(marks.items(), key=lambda x: sum(x[1])))
print(ans1)
