"""
Question 61

Given a list, remove all duplicate elements while
preserving the original order of the unique items.
""" 

def remove_duplicates(lst):
    result = []
    for i in range(0, len(lst)):
        if lst[i] not in result:
            result.append(lst[i])
    return result


data = [10, 20, 30, 20, 10, 40, 50,40]
print(remove_duplicates(data))
print(data, id(data))