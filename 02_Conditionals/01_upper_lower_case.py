word = input("Enter a Word: ")

if word.isupper():
    print("The Character is Uppercase")
elif word.islower():
    print("The Character is Lowercase")
elif word.isalpha():
    print("The Character is Mixed case")
else:
    print("The Character is not an Alphabet")
