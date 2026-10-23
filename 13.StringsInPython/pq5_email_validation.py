"""
Q97: Email Validation

Take an email as input. Validate that it contains exactly one @ and at least
one (. dot) . Print "Valid" or "Invalid".
"""

# email = input("Enter your email : ")

# atrate_count = 0
# dot_count = 0

# for ch in email:
#     if ch == "@":
#         atrate_count += 1
#     if ch == ".":
#         dot_count += 1

# if atrate_count == 1 and dot_count >= 1:
#     print("Valid")
# else:
#     print("Invalid")


def check_email(email: str):
    if email.count("@") == 1 and "." in email:
        return True
    return False


email = "priyanshu@gmail.com"
print(check_email(email))
