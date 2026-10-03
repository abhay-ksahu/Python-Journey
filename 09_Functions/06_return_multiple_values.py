def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    if b != 0:
        division = a / b
    else:
        division = "Undefined (cannot divide by zero)"

    return addition, subtraction, multiplication, division

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    add, diff, mult, divi = calculate(a, b)

    print(f"Addition:       {add}")
    print(f"Subtraction:    {diff}")
    print(f"Multiplication: {mult}")
    print(f"Division:       {divi}")
except ValueError:
    print("only numbers are allowed as input!")