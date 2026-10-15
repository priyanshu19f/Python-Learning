# Make a function which return min and max of a list


def min_max(lst):
    # logic
    mini = min(lst)
    maxi = max(lst)
    return mini, maxi


lst = [12, 14, 1, 85, 6]
mini, maxi = min_max(lst)
print(f"minimum number : {mini}")
print(f"maximum number : {maxi}")
