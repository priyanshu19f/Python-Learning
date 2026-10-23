"""
Q109: PAN Card Validation(Homework)
Take a string as input. Check if it is a valid Indian PAN card number.
Format: 5 uppercase letters + 4 digits + 1 uppercase letter (Total 10
characters). Example: ABCDE1234F.
"""


def check_valid(pan: str):
    if len(pan) != 10:
        return "invalid"
    start = pan[0:5]
    mid = pan[5:9]
    end = pan[-1]
    if start.isalpha() and mid.isdigit() and end.isalpha():
        return "valid"
    else:
        return "invalid"


pan = "ABCDE1234F"
print(check_valid(pan))
