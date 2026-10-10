unit = int(input("Enter Unit: "))

if unit <= 100:
    t1 = unit*5
    bill = t1

elif unit <= 200:
    t1 = 100*5
    t2 = (unit - 100)*7
    bill = t1 + t2

elif unit <= 300:
    t1 = 100*5
    t2 = 100*7
    t3 = (unit - 200)*10
    bill = t1 + t2 + t3

else:
    t1 = 100*5
    t2 = 100*7
    t3 = 100*10
    t4 = (unit - 300)*15
    bill = t1 + t2 + t3 + t4

print(f"The Electricity bill is: {bill}")
