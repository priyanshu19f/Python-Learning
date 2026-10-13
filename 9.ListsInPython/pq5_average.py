"""
Question 55: Calculate the Average

Given a list of numbers, use a loop to calculate and print their 
average. You can use len() to get the count of elements, but avoid using sum() for the total.
"""

def calculate_avg(lst):
    total = 0
    for num in lst :
        total += num
    avg = total / len(lst)
    return avg

lst = [85, 90,78,92,88]
print(f"Average : {calculate_avg(lst)}")