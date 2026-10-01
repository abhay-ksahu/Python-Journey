percentage = float(input("Enter your Percentage: "))

if percentage < 0 or percentage > 100:
    print("The Given percentage is not valid")

elif percentage >= 75:
    print("The student is passed with Grade A")

elif percentage >= 50:
    print("The student is passed with Grade B")

elif percentage >= 35:
    print("The student is passed with Grade C")

else:
    print("The student is Failed")
