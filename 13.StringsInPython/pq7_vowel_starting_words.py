"""
Q99: Vowel-Starting Words
Take a sentence as input. Split it into words and print how many words
start with a vowel.
"""


def count_vowel_words(sentence: str):
    vowels = "aeiouAEIOU"
    words = sentence.split()
    ans = 0
    for word in words:
        if word[0] in vowels:
            ans += 1
    return ans


# sen = input("Enter a sentence : ")
sen = "My name is Priyanshu Gupta and is I am a very good coder"
print(count_vowel_words(sen))
