while True:
    try:
        num1 = float(input("Enter your first number: "))
        valid_operation = ["+", "-", "*", "**", "/", "%", "//" ]
        while True:
            operation = input("Enter your operator: ")
            if operation in valid_operation:
                break
            else:
                print("please enter valid operation")
        num2 = float(input("Enter your second number: "))

        if operation == "+":
            print(num1 + num2)

        elif operation == "-":
            print(num1 - num2)

        elif operation == "*":
            print(num1 * num2)

        elif operation == "**":
            print(num1 ** num2)

        elif operation == "/":
            print(num1 / num2)

        elif operation == "%":
            print(num1 % num2)

        elif operation == "//":
            print(num1 // num2)

        choice = input("Do you want to continue? (yes/no): ")

        if choice.lower() == "no":
            print("Calculator closed")
            break

    except ValueError:
        print("please enter valid numbers")

    except ZeroDivisionError:
        print("Cannot divide by zero")
