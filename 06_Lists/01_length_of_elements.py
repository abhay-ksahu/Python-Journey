# Largest Element
user_input = input("Enter elements using spaces: ")
elements = user_input.split()

largest_element = ""
len_element = 0

for element in elements:
    if len(element) > len_element:
        largest_element = element
        len_element = len(element)
print(f"Largest element in list: {largest_element}")
print(f"length of element:{len_element}")

# Smallest Element

user_input = input("Enter elements using spaces: ")

elements = user_input.split()

smallest_element = ""
len_element = float("inf")   # float("inf") --> Positive Infinity

for element in elements:
    if len(element) < len_element:
        smallest_element = element
        len_element = len(element)

print(f"Smallest element in list: {smallest_element}")
print(f"Length of element: {len_element}")

# Second largest number
elements = list(map(int, input("Enter numbers using spaces: ").split()))
unique_elements = list(set(elements))
unique_elements.sort()
print(unique_elements)
print(f"Second largest numbers: {unique_elements[-2]}")