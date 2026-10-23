"""
Q95. Read a sentence from the user. Count and print the total number of
vowels (a, e, i, o, u, case-insensitive) present in it, using a for loop. (HW)
"""

text = input("Enter a sentence : ")
count_vowels = 0
for ch in text:
    if ch in "AEIOUaeiou":
        count_vowels += 1
print(f"vowels : {count_vowels}")
