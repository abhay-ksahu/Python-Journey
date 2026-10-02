txt = input("Enter sentence: ")
target = input("Enter character: ")

sentence = txt.lower()
occurrence = 0
for char in sentence:
    if char == target:
        occurrence += 1

print(occurrence)