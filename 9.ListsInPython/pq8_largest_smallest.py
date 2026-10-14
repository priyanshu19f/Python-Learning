"""
Q58. Find the largest and smallest number
in a list without using built-in functions like
max() or min().
"""

def largest_smallest(lst):
    largest = float("-inf")
    smallest = float("inf")

    for ele in lst:
        if ele > largest:
            largest = ele
        if ele < smallest:
            smallest = ele
    return largest, smallest


nums = [4, 7, 3, 8, 1, 1, 2, 10, 9, 6, 9, 1, 1, 1]

print(largest_smallest(nums))