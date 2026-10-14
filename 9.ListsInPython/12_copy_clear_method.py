original_list = [10,20,30]
new_list = original_list.copy() # Creates an independent copy

new_list.append(40) # Modifies 'new_list'
print(original_list, id(original_list)) # Output: [10, 20, 30] -'original_list' remains unchanged
# Output: [10,20,30,40]

print(new_list, id(new_list))



my_list = ["apple", "banana", "cherry"]
print(f"before clear : {my_list}, id={id(my_list)}")
my_list.clear()
print(f"after clear : {my_list}, id={id(my_list)}")