numbers = [10,20,20,30,40,50,50]

duplicate = []

for number in numbers:
    if numbers.count(number) > 1 and number not in duplicate:
        duplicate.append(number)
print(duplicate)