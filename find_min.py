def find_minimum(lst):
    if not lst:
        raise ValueError("Cannot find minimum of an empty list")
    
    min_elem = lst[0]
    for num in lst[1:]:
        if num < min_elem:
            min_elem = num
    return min_elem


numbers = [8, 3, 5, -2, 7, 0, -10, 4]
minimum = find_minimum(numbers)
print("Minimum element:", minimum)
