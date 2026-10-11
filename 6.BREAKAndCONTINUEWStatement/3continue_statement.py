i=1 
while i<=10:
    if i==5:
        i+=1
        continue
    print(i,end=" ")
    i+=1


print()

j = 0
while j<=10:
    j += 1
    if j % 2 == 0:
        continue
    print(j,end=" ")