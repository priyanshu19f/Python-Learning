"""
Q66. Using list comprehension, create a list of squares of all odd numbers from 1 to 20.
""" 
odd_squares_list = [i*i for i in range(1,21) if i%2!=0]
print(odd_squares_list)