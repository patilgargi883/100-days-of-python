def find_second_largest(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements.")
    
    first = second = float('-inf')
    
    for num in lst:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    if second == float('-inf'):
        raise ValueError("There is no second distinct largest element.")
    
    return second

# Example usage
numbers = [10, 20, 4, 45, 99, 99]
try:
    result = find_second_largest(numbers)
    print("Second largest element:", result)
except ValueError as e:
    print(e)
