def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
num = int(input("Enter your number: "))
print(even_odd(num))