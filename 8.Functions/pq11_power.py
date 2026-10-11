"""
Q47. Write a function power(base, exp) that returns base raised to exp using a
loop - no ** operator or pow() allowed.
"""

def power(base, exp):
    ans = base
    for i in range(1, exp):
        ans *= base 
    return ans

print(power(5,3)) 