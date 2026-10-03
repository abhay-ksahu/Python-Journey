def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


try:
    celsius = float(input("Enter temperature in Celsius: "))

    fahrenheit = celsius_to_fahrenheit(celsius)

    print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")

except ValueError:
    print("Please enter a valid number!")