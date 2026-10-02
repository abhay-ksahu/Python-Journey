def factorial(n):
    if n < 0:
        return None

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is {factorial(num)}")