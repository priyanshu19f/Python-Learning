"""
Q19. Ask a number from the user, and print all the factors.
"""


n = int(input("Enter a number : "))

i=1
while i<=n:
    if n%i==0:
        print(i, end=" ")
    i += 1