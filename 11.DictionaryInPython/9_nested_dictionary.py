students = {
    "101": {"name": "Rahul", "age": 21, "city": "Delhi"},
    "102": {"name": "Priya", "age": 20, "city": "Mumbai"},
    "103": {"name": "Karan", "age": 22, "city": "Pune"},
    # "104": {
    #     "name": "Karan",
    #     "age": 22,
    #     "city": "Pune",
    #     "details": {
    #         "phone": 234567892,
    #         "gender": "male",
    #     },
    # },
}

# how to access
print(students["101"])
print(students["102"]["name"])
print(students["103"]["city"])
# print(students["104"]["details"]["phone"])


for roll_no, details in students.items():
    print(f"roll no : {roll_no} and details : {details}")


for roll_no, details in students.items():
    print(f"roll no : {roll_no} , name : {details['name']} , age : {details['age']}")
