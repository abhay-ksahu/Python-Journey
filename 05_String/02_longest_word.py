# Longest word
sentence = input("Enter sentence: ")

words = sentence.split()

longest_word = ""
longest_length = 0

for word in words:
    if len(word) > longest_length:
        longest_word = word
        longest_length = len(word)
print(f"The longest word in sentence: {longest_word}")
print(f"The longest length in sentence: {longest_length}")