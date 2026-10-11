# Age >= 18
#  Certificate -> True     

age = 45
certificate = False

if age >= 18 :
    if certificate == True:
        print("You will be hired")
    else : 
        print("Cannot hire, certificate is missing")
else : 
    print("Cannot hire, age less than 18")