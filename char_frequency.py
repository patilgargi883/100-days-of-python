def char_frequency(text):
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

# Example usage
user_input = input("Enter a string: ")
frequency = char_frequency(user_input)

print("Character Frequencies:")
for char, count in frequency.items():
    print(f"'{char}': {count}")
