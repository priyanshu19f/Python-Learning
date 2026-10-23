"""
Q103: Username Validation

Take a username as input. Strip any spaces from both sides and check if the
cleaned name starts with a letter (not a digit). Print "Valid" or "Invalid".
"""


def check_username(user: str):
    user = user.strip()
    if user[0].isalpha():
        print("Valid")
    else:
        print("Invalid")


username = " priyututor     "
username = " 2priyututor     "
check_username(username)
