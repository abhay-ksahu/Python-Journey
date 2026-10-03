
def validate_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_characters = "!@#$%^&*()-_+="

    for char in password:
        if char.isupper():
            has_upper = True

        elif char.islower():
            has_lower = True

        elif char.isdigit():
            has_digit = True

        elif char in special_characters:
            has_special = True

    if (
        len(password) >= 8
        and has_upper
        and has_lower
        and has_digit
        and has_special
        and " " not in password
    ):
        return True
    else:
        return False


password = input("Enter your password: ")

if validate_password(password):
    print("Password is valid and fulfills all requirements!")
else:
    print("Password does not meet all requirements.")