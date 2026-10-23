"""
Q107: Reverse Word Order

Take a sentence as input. Reverse the order of words (not the characters in each
word). Example: "Python is fun" -> "fun is Python".
"""


def rev_word_order(text: str):
    text = text.split()
    text = text[::-1]
    text = " ".join(text)
    print(text)


text = "Python is fun"
rev_word_order(text)
