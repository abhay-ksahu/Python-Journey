sentence = input("Enter sentence: ").strip()

for char in sentence:
    if sentence.count(char) == 1:
        print("First non-repeating character:", char)
        break
else:
    print("No non-repeating character found.")