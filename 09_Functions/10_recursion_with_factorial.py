def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1

    return n * factorial(n-1)
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial of negative number is not defined!")
else:
    print(f"Factorial of {num} is {factorial(num)}")