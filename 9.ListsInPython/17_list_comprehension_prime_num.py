# make a list from 1 to 100 of only prime numbers using list comprehension


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


prime = [i for i in range(2, 101) if is_prime(i)]
print(prime)
