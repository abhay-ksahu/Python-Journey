words = ["apple", "ant", "banana", "mango", "monkey", "mouse", "doctor"]

group = {}

for word in words:
    first_letter = word[0]
    if first_letter not in group:
        group[first_letter] = []

    group[first_letter].append(word)
print(group)