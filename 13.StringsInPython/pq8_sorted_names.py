"""
Q100: Sorted Names

Take a list of names as input (comma separated). Split them, sort them
alphabetically, and join them back with " I" as separator.
"""

names = "priyanshu,anuj,rohan,rishu,rekha"
names = " | ".join(sorted(names.split(",")))
print(names)
