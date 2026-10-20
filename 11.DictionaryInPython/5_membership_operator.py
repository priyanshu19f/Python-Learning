student = {
    "name": "Priyanshu",
    "age": 30,
    "gender": "male",
    "city": "Gorakhpur",
}

print("name" in student)
print("state" in student)
print("state" not in student)


k = input("Enter a key : ")
if k in student:
    print(f"{k} : student[k]")
else:
    print(f"{k} does not exist in student")
