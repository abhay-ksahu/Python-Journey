num = int(input("Enter your number: "))

rev_num = 0

while(num > 0):
    digit = num % 10
    rev_num = rev_num*10 + digit
    num = num // 10

print(f"Reversed number is: {rev_num}")