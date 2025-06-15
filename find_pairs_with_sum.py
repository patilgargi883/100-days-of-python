def find_pairs_with_sum(numbers, target):
    seen = set()
    pairs = set()

    for num in numbers:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)

    return list(pairs)

# Take user input
nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target sum: "))

result = find_pairs_with_sum(nums, target)
print("Pairs with sum", target, ":", result)
