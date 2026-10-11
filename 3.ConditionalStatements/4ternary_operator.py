age = int(input("Enter age : "))

# if age >=18:
#     status = "Adult"
# else : 
#     status = "Minor"

status = "Adult" if age>=18 else "Minor"

print(f"your status is {status}")