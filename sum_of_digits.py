def sum_of_digits(n):
    n = abs(n)  # Handle negative numbers
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# Example usage
number = 12345
result = sum_of_digits(number)
print("Sum of digits:", result)
