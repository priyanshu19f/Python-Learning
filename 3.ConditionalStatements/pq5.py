"""
Q11: Take a person's age and whether they have a valid ID (True/False) as input. They
can enter a venue only if they are 18 or older AND have a valid ID. Print the
appropriate message.
"""

age = int(input("Enter age : "))
# id = bool(input("Have valid id(True/False) : "))
id = input("Have valid id(True/False) : ")

if age >= 18 and id=="True" : 
    print("You can enter")
else : 
    print("You cannot enter")








"""
NOTE: bool(input()) trap

input() always returns a string, and bool() only checks if it's empty.
    bool("")      -> False
    bool("False") -> True   (non-empty string)

Fix: compare the string instead.
    has_id = input("Have valid id(True/False) : ").strip().lower() == "true"
"""