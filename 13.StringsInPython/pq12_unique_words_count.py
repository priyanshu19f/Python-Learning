"""
Q104: Unique Words Count
Take a paragraph as input. Print the count of unique words in it (case insensitive).
"""


def count_unique_words(para: str):
    words = para.split()
    return len(set(words))


paragraph = "The quick brown fox jumps over the lazy dog. The dog was lazy but the fox was quick"
print(count_unique_words(paragraph))
