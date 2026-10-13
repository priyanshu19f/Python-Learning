#       0     1    2    3    4    5    6    7    8    9   10
#       -11   -10 -9  -8 -7  -6   -5   -4   -3   -2  -1
lst = [56, 39, 21, 99, 53, 18, 64, 69, 88, 20, 11]

lst1 = lst[0:4]
lst1 = lst[4:8]
lst1 = lst[1:10] 
lst1 = lst[1:99]        # no index error
lst1 = lst[4:5] 
lst1 = lst[5:5] 

lst1 = lst[3: ] 
lst1 = lst[ : 6] 
lst1 = lst[1 : 10 : 2] 
lst1 = lst[0 :  : 2] 
lst1 = lst[ :  : 3] 
print(lst1) 



#       0     1    2    3    4    5    6    7    8    9   10
#       -11   -10 -9  -8 -7  -6   -5   -4   -3   -2  -1
lst = [56, 39, 21, 99, 53, 18, 64, 69, 88, 20, 11]
lst2 = lst[9 : 2 : -1]
lst2 = lst[5 :  : -1]

#  print entire list in reverse order
lst2 = lst[ :  : -1]
print(lst2)