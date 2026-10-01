word = input("Enter your word: ")

palindrome = word[::-1]

if word.lower() == palindrome.lower():
    print("The word is palindrome")
else:
    print("The given word is not a palindrome")