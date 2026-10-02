elements = list(map(int, input("Enter numbers using spaces: ").split()))

for i in range(len(elements)):
    for j in range(i + 1, len(elements)):
        if elements[i] > elements[j]:
            elements[i], elements[j] = elements[j], elements[i]

print(f"Sorted list: {elements}")