"""
Create a list of 5 of your favourite movies. Print the first, last, and middle movie from your list using both positive and negative indexing where appropriate.

# Example Output (using hypothetical movie list):
# First movie: The Shawshank Redemption
# Middle movie: The Matrix
# Last movie: Forrest Gump
"""

movies = [
    "The Shawshank Redemption",
    "Spiderman",
    "The Matrix",
    "Antman",
    "Forrest Gump",
    "Avengers",
    "Iron Man",
]
n = len(movies)
# positive indexing
print(f"first movie : {movies[0]}")
print(f"middle movie : {movies[n//2]}")
print(f"last movie : {movies[n-1]}")

# negative indexing
print(f"first movie : {movies[-n]}")
print(f"middle movie : {movies[(-n//2)-1]}")
print(f"last movie : {movies[-1]}")
