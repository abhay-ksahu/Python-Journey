def check_positive_negative(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def check_prime(number):
    if number < 2:
        return "Not Prime"

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return "Not Prime"
    return "Prime"

def count_digit(number):
    return len(str(abs(number)))

def number_analyze(number):
    print("----------Number Analysis----------")
    print(f"Number: {number}")
    print(f"Type: {check_positive_negative(number)}")
    if number != 0:
        print(f"Even/Odd: {check_even_odd(number)}")

        print(f"Prime Status: {check_prime(number)}")

        print(f"Number of digit: {count_digit(number)}")\

number = int(input("Enter Number: "))
number_analyze(number)