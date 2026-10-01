# Largest Digit
num = int(input("Enter your number: "))

largest_digit = 0

while num > 0:
    digit = num % 10 
    largest_digit = max(largest_digit, digit)
    num = num // 10
print(f"The largest in numbers is: {largest_digit}")

# Smallest digit

num = int(input("Enter your number: "))

smallest_digit = 9

while num > 0:
    digit = num % 10
    smallest_digit = min(smallest_digit, digit)
    num = num // 10

print(f"The smallest digit is: {smallest_digit}")