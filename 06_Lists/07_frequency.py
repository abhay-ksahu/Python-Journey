numbers = [1,2,3,4,5,5,6,6,7,7,7,7]

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] +=1
    else:
        frequency[number] = 1
print(frequency)