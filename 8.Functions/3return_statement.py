def addition(n1, n2, n3):
    return n1+n2+n3

sum = addition(20, 34, 23)
print(sum)


def can_vote(age):
    if(age>=18):
        return True
    else : 
        return False

ans = can_vote(20)
print(f"can vote : {ans}")

print(can_vote(11))