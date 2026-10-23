text = "Programming"

# in / not in

print("p" in text)
print("P" in text)
print("z" not in text)
print("m" not in text)
print("gram" in text)


print("Vowels count : ", end=" ")
count_vowel = 0
# for ch in text:
#     ch = ch.lower()
#     if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
#         count_vowel += 1

vowel = "AEIOUaeiou"
for ch in text:
    if ch in vowel:
        count_vowel += 1

print(count_vowel)
