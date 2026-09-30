from datetime import date, time

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

today = date.today()
age = today.year - birth_year

if (today.month, today.day)<(birth_month, birth_day):
    age -= 1
print(f"Age of the person is: {age}")