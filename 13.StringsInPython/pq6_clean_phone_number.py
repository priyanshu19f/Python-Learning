"""
Q98: Clean Phone Number

Take a phone number as input in the format +91-98765-43210. Remove all
dashes and the country code. Print the cleaned 10-digit number.
"""

phone = "+91-98765-43210"
clean_phone = ""
if phone.startswith("+91"):
    clean_phone = phone.replace("+91", "")
    clean_phone = clean_phone.replace("-", "")
print(clean_phone)
