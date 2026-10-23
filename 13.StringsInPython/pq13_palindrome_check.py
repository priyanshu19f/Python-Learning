"""
Q105: Palindrome Check
Write a function is_palindrome(text) that returns True if the given string is a
palindrome (ignoring case and spaces).
"""


def is_palindrome(text: str):
    text = text.lower().replace(" ", "")
    reverse = text[::-1]
    if text == reverse:
        return True
    else:
        return False


text = paragraph = "naman aka naman"
print(is_palindrome(text))
print(is_palindrome("Never odd or even"))
print(is_palindrome("racecar"))
print(is_palindrome("Hello"))
