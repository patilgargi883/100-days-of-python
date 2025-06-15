def find_largest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# Take input from user
sentence = input("Enter a sentence: ")
largest_word = find_largest_word(sentence)

print("Largest word:", largest_word)
