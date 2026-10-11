# Return True if a number is prime number return False

def is_prime(n):
    for i in range(2,n):
        if n % i ==0 :
            return False
    return True

print(is_prime(55))
print(is_prime(53))