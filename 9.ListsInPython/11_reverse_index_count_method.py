nums = [4, 7, 3, 8, 1, 1, 2, 10, 9, 6, 9, 1, 1, 1]

print(f"Original List : {nums}, id : {id(nums)}")
nums.reverse()
print(f"Reverse List : {nums}, id : {id(nums)}")

# [1, 1, 1, 9, 6, 9, 10, 2, 1, 1, 8, 3, 7, 4]
print(nums.index(10))
print(nums.count(1))
print(nums.count(100))