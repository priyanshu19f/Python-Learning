"""
Q102: Longest Word

Take a sentence as input. Print the longest word in it.
"""

# sen = "Take a sentence as input. Print the longest word in it"
sen = input("Enter sentence : ")

sen = sen.split()

longest_count = 0
longest_word = ""
for word in sen:
    if len(word) > longest_count:
        longest_count = len(word)
        longest_word = word

print(longest_word)
