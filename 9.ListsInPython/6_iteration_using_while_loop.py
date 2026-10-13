nums = [5,7,4, 64, 32, 17, 53, 85, 3, 1, 999]
i = 0
while i<len(nums):
    print(nums[i], end=" ")
    i += 1

print()

# reverse iteration 
j = len(nums)-1
while j>=0 : 
    print(nums[j],end=" ")
    j -= 1

print()

# using negative indexing
k = len(nums)
m = -1
while m>= (-k):
    print(nums[m], end=" ")
    m -= 1