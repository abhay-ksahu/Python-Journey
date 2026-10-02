numbers = list(map(int, input("Enter numbers using spaces: ").split()))

target = int(input("Enter target: "))

found = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):

        if numbers[i] + numbers[j] == target:
            print("Pair:", numbers[i], numbers[j])
            found = True

if not found:
    print("No such pair exists!")