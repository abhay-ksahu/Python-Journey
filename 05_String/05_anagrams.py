word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

word1 = word1.lower()
word2 = word2.lower()

if sorted(word1) == sorted(word2):
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")