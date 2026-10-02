elements = list(map(int, input("Enter elements using spaces: ").split()))
even_numbers = []
odd_numbers = []

for element in elements:
    if element % 2 == 0:
        even_numbers.append(element)
    elif element % 2 != 0:
        odd_numbers.append(element)

print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")