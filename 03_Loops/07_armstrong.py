num = int(input("Enter your number: "))

original = num
digits = len(str(num))
armstrong = 0

while num > 0:
    digit = num % 10
    armstrong = armstrong + digit ** digits
    num = num // 10

if original == armstrong:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")