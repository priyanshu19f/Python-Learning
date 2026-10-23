"""
CASE CONVERSION
upper(): Converts all characters in the string to uppercase.
lower(): Converts all characters in the string to lowercase.
title(): Converts the first character of each word to uppercase and the remaining to lowercase.
capitalize(): Converts only the first character of the entire string to uppercase and the rest to lowercase.
swapcase(): Swaps the case of each character - uppercase becomes lowercase and vice versa.
"""

text = "Priyanshu Gupta is a coder"
print(text, id(text))

upper = text.upper()
print(upper, id(upper))

lower = text.lower()
print(lower, id(lower))

title = text.title()
print(title, id(title))

capitalizee = text.capitalize()
print(capitalizee, id(capitalizee))

swap_case = text.swapcase()
print(swap_case, id(swap_case))
