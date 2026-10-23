"""
String Methods: Searching and Replacing
count(): Substring Frequency
find(): Locate First Occurrence
index(): Locate (with Error)
replace(): Substitute Substrings
"""

text = "Priyanshu Gupta is a coder"

print(text.count("a"))
print(text.count("an"))


print(text.find("a"))
print(text.find("coder"))
print(text.find("python"))


print(text.index("a"))
# print(text.index("z"))            ValueError: substring not found

print(text, id(text))
txt = text.replace("coder", "developer")
print(txt, id(text))
