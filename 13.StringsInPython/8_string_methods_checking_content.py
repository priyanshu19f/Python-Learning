"""
CHECKING CONTENT (T/F)
isalpha(): All Letters?
isdigit(): All Digits?I
isalnum(): AlphaNumeric Only?
isspace(): All Whitespace?
startswith() and endswith()
"""

text = "Priyanshu Gupta"
# text = "PriyanshuGupta"
print(text.isalpha())

text1 = "289392"
print(text1.isdigit())

text2 = "sdlj943934alfla"
print(text2.isalnum())

text3 = "              \n\t   "
print(text3.isspace())


name = "Priyanshu Gupta"
print(name.startswith("Pri"))
print(name.startswith("ri"))

print(name.endswith("pta"))
print(name.endswith("z"))


age = input("Enter age : ")
if age.isdigit():
    if int(age) >= 18:
        print("You can vote")
    else:
        print("You cannot vote")
else:
    print("Pleae enter valid age")
