lst = ["Priyanshu", "Archit", "Suresh", 55, 46.335, True]

print(lst, id(lst))

# append 
lst.append("Hello")
lst.append(340)
print(lst)

# insert 
# ['Priyanshu', 'Archit', 'Suresh', 55, 46.335, True, 'Hello', 340]
lst.insert(2,"Delhi")
print(lst)

# pop -> by index
# ['Priyanshu', 'Archit', 'Delhi', 'Suresh', 55, 46.335, True, 'Hello', 340]
x = lst.pop()
print(x)
lst.pop(3)
print(lst, id(lst))

# remove -> by value
lst.remove("Archit")
print(lst, id(lst))
