# Shortest word
sentence = input("Enter sentence: ")

words = sentence.split()

if not words:
    print("No words were entered.")

else:
    shortest_word = words[0]
    shortest_length = len(shortest_word)

    for word in words[1:]:
        if len(word) < shortest_length:
            shortest_word = word
            shortest_length = len(word)

    print(f"The shortest word in sentence: {shortest_word}")
    print(f"The shortest length in sentence: {shortest_length}")