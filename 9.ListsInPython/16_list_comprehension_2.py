# 1 to 20 only even numbers 

even_list = [i for i in range(1,21) if i%2==0] 
new_list = [i for i in range(1,100) if i%3==0 and i%7==0] 
print(even_list) 
print(new_list)