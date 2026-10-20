"""
Q87. Student Details

Create a nested dictionary containing details for 4 students, where each
student entry includes their name, age, and city. Write a loop to print the
full details of each student in a clear, readable format.
"""

stu_details = {
    101: {"name": "Priyanshu", "age": 22, "city": "Salempur"},
    102: {"name": "Ram", "age": 21, "city": "Deoria"},
    103: {"name": "Mohan", "age": 23, "city": "Salempur"},
    104: {"name": "Shyam", "age": 22, "city": "Gorakhpur"},
}


for roll_no, details in stu_details.items():
    print(f"Roll No. : {roll_no}")
    for k, v in details.items():
        print(f"{k} : {v}")
    print()
