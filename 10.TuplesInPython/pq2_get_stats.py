"""
Q78: Write a function get_stats (nums) that takes a tuple of
numbers and returns a tuple containing the sum, average, minimun
Unpack the returned tuple and print each value.
"""


def get_stats(nums):
    total = sum(nums)
    avg = total / len(nums)
    mini = min(nums)
    return total, avg, mini


my_tuple = (45, 25, 54, 52, 12)
summ, average, minimum = get_stats(my_tuple)
print(f"Sum : {summ} , average : {average}, minimum : {minimum}")
