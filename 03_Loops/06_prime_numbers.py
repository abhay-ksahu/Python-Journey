num = int(input("Enter your number: "))

if num < 2:
    print("The given numbers is not an prime number!")

else:
    is_prime = True

    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("The given number is prime number!")
    else:
        print("The given numbers is not an prime number!")
