nums = [5,7,4, 64, 32, 17, 53, 85, 3, 1, 999]
n = len(nums)

for i in range(0,n):
    print(nums[i], end=" ")

total = 0
for i in range(0,n):
    total += nums[i]

print(f"\nTotal sum : {total}")

# By value 
for i in nums:
    print(i,end=" ")

total = 0
for num in nums : 
    total += num

print(f"\nTotal sum : {total}")



# reverse iteration using By value 
for num in nums[: : -1]:
    print(num,end= " ")