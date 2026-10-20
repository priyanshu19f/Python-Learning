student = {
    "name": "Priyanshu",
    "age": 22,
}
print(student, id(student))


# updating
student["age"] = 30

# adding
student["gender"] = "male"

# using method
student.update(
    {
        "city": "Gorakhpur",
        "phone": 5426625632,
        "state": "Uttar Pradesh",
    }
)

print(student, id(student))
