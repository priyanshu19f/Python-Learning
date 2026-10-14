nums = [4, 7, 3, 8, 1, 1, 2, 10, 9, 6, 9, 1, 1, 1]

# sorted 
print(f"Original List : {nums}, id : {id(nums)}")
new_list  = sorted(nums) 
print(f"Sorted List : {new_list}, id : {id(new_list)}")


# sort 
# print(f"Original List : {nums}, id : {id(nums)}")
nums.sort()
print(f"Original List after sort method : {nums}, id : {id(nums)}")
