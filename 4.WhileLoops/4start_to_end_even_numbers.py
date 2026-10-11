start=int(input("Enter start : "))
end=int(input("Enter end : "))

i=0
if(start%2!=0):
    i = start+1
else : 
    i = start

while i<=end:
    print(i, end=" ")
    i+=2