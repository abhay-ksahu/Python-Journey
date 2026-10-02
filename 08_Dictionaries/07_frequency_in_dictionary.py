numbers = [1,2,3,3,3,4,4,5,6,7,7,7,8,9]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print(frequency)