def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

# Example usage
number = 16
if is_power_of_two(number):
    print(f"{number} is a power of two.")
else:
    print(f"{number} is not a power of two.")
