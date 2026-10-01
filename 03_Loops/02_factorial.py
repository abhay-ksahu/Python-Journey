   
try:
    n = int(input("Enter tha value: "))

    if n < 0:
        print("Factorial is not defined for negative numbers")
    else:
        factorial = 1

        for i in range(1,n+1):
            factorial *= i
        print(f"Factorial of {n} = {factorial}")
except ValueError:
    print("Please enter only numbers!")