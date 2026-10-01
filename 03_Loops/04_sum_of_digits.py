num = int(input("Enter your number: "))

sum_digit = 0

while num > 0:
    digit = num % 10
    sum_digit = sum_digit + digit
    num = num // 10

print(f"The sum of all digits in number is: {sum_digit}")