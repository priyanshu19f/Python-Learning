"""
String Methods: Splitting and Joining
split(): Break String into List
join(): Combine List into String
"""

# split
text = "Priyanshu Gupta is a coder"

print(list(text))
print(text.split())

# count number of words
print(len(text.split()))

text = "apple,mango,banana,cherry"
print(text.split(","))


# join
my_name = ["p", "r", "i", "y", "a", "n", "s", "h", "u", 5, 55.5, "coder"]
# ans = " ".join(my_name)
ans = "-".join(str(ch) for ch in my_name)
print(ans, type(ans))
