from collections import Counter

# Take user input
text = input("Enter a string: ")

# Count character frequency
frequency = Counter(text)

# Display results
for char, count in frequency.items():
    print(f"'{char}': {count}")
