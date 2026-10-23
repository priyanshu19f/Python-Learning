text = "Programming"

n = len(text)
for i in range(0, n):
    print(text[i], end="-")

print()
for char in text:
    print(char, end="_")

print()
# while loop
j = 0
while j != n:
    print(text[j], end=" ")
    j += 1


print()
for i, ch in enumerate(text):
    print(f"index : {i} and character : {ch}")
