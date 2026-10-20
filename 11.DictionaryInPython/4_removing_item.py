student = {
    "name": "Priyanshu",
    "age": 30,
    "gender": "male",
    "city": "Gorakhpur",
    "phone": 5426625632,
    "state": "Uttar Pradesh",
}
print(student, id(student))

# pop
student.pop("state")
print(student, id(student))

# clear
student.clear()
print(student, id(student))

# del
del student["age"]
print(student, id(student))


del student  # delete the dictionary / any variable
