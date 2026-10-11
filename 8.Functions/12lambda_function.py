"""
A lambda function is a small anonymous function written in a single line. It
is useful when you need a simple function for a short period and do
not want to formally define it with def.
"""

# def square(num):
#     return num * num

square = lambda num : num * num

print(square(10))
print(square(15))


# Return True if age>=18 else false
# def is_adult(age):
#     if age >= 18:
#         return True
#     return False

is_adult = lambda age : True if age>=18 else False
print(is_adult(22))