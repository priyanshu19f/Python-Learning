# make a new list from 1 to 10 -> [1, 2, 3, .... 10 ]

# new_list = []
# for i in range(1,11):
#     new_list.append(i)

new_list = [i for i in range(1,11)]

print(new_list) 


neg_list = [i for i in range(10,0,-1)]
print(neg_list) 

# 1 to 10 all squares
sq_list = [a*a for a in range(1,11)]
print(sq_list) 