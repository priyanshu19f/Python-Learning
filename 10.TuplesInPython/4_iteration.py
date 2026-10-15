my_tuple = (45, 32, 11, "Priyanshu", "Khurana", "Surat", 99)
n = len(my_tuple)
# method 1
for i in range(0, n):
    print(my_tuple[i], end=" ")

print()

# method 2
for item in my_tuple:
    print(item, end=" ")

print()
# method 3
for idx, item in enumerate(my_tuple):
    print(f"index : {idx} , value : {item}")
