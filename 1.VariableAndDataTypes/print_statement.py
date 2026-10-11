name = 'priyanshu'
age = 22
gender = 'male'

print("Hello",name,"your age is",age,"and gender is",gender)

# cannot add + string and int
# print("Hello "+name+" your gender is "+gender+" and age is "+age)

print(name,age,gender)
print(name,age,gender, sep="--")


print(name, end=" ")
print(age, end=" ")
print(gender)


# F-Strings 
print(f"Your name is {name}, age is {age} and gender is {gender}")
print(f"Your name is {name}, age is {age+25} and gender is {gender}")
print(age)