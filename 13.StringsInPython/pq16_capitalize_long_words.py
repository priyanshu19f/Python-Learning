"""
Q108: Capitalize Long Words
Take a sentence as input. Capitalize only the first letter of each word
that is longer than 3 characters. Keep the rest as is.
"""


def capitalize_word(text: str):
    text = text.split()
    for i in range(0, len(text)):
        if len(text[i]) > 3:
            text[i] = text[i].capitalize()
    return " ".join(text)


text = "Python is a very good language and is widely used"
print(capitalize_word(text))
