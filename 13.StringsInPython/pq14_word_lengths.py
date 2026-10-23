"""
Q106: Word Lengths
Take a sentence as input. Print each word's length next to it. Example: Python (6)
is (2) great (5).
"""


def word_len(text: str):
    text = text.split()
    print(text)
    for i in range(0, len(text)):
        text[i] = text[i] + " " + str(len(text[i]))
    print(" ".join(text))


text = "Python is great"
word_len(text)
