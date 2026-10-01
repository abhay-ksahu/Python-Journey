a = int(input("Enter base (a): "))
b = int(input("Enter exponent (b): "))

result = 1

for i in range(b):
    result = result*a
print(f"{a}^{b} = {result}")