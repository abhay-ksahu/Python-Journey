sentence = input("Enter sentence: ")

txt = sentence.split()
reversed_sentence = []

for word in txt:
    reversed_sentence.append(word[::-1])

result = " ".join(reversed_sentence)
print(result)
    
