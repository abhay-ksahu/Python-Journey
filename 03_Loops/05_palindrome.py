try:
    num = int(input("Enter your number:"))

    palindrome = num[::-1]

    if num == palindrome:
        print("The number is palindrome")
    else:
        print("The given number is not a palindrome")
except ValueError:
    print("Please try only numbers!")
except TypeError:
    print("Please enter more than 1 character!")


# Code 2

try:
    num = int(input("Enter your number: "))

    original = num
    palindrome = 0

    while num > 0:
        digit = num % 10
        palindrome = palindrome * 10 + digit
        num = num // 10

    if original == palindrome:
        print("The number is a palindrome")
    else:
        print("The given number is not a palindrome")

except ValueError:
    print("Please enter numbers only!")