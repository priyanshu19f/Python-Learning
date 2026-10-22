allowed_users = {"Priyanshu", "Rohan", "Shyam"}

user = input("Enter your name : ").capitalize()

if user in allowed_users:
    print("Access Granted")
else:
    print("Access Denied")
