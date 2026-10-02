elements = list(map(int, input("Enter elements using spaces: ").split()))

new_list = []

for element in elements:
    if element not in new_list:
        new_list.append(element)
print(f"List with unique elements: {new_list}")