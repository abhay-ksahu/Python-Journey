text = input("Enter a message: ")

vowel_count = 0
consonant_count = 0
space_count = 0
digit_count = 0
uppercase_count = 0
lowercase_count = 0
special_count = 0

for char in text:

    if char.lower() in "aeiou":
        vowel_count += 1

    elif char.isalpha():
        consonant_count += 1

    elif char.isspace():
        space_count += 1

    elif char.isdigit():
        digit_count += 1
        
    if char.isupper():
        uppercase_count += 1

    if char.islower():
        lowercase_count += 1

    if not char.isalpha() or not char.isdigit() or not char.isspace():
        special_count += 1

print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")
print(f"Number of spaces: {space_count}")
print(f"Number of digits: {digit_count}")
print(f"Number of uppercase: {uppercase_count}")
print(f"Number of lowercase: {lowercase_count}")
print(f"Number of Special character: {special_count}")
