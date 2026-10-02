word = input("Enter word: ")
count_vowel = 0

for char in word:
    if char.lower() in "aeiou":
        count_vowel += 1
print(count_vowel)
