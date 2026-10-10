weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

# BMI Calculation
BMI = weight / (height ** 2)

if BMI < 18.5:
    print(f"Your BMI is {BMI:.2f} and you are UNDERWEIGHT")

elif BMI < 25:
    print(f"Your BMI is {BMI:.2f} and you are HEALTHY")

elif BMI < 30:
    print(f"Your BMI is {BMI:.2f} and you are OVERWEIGHT")

else:
    print(f"Your BMI is {BMI:.2f} and you are OBESE")
    
