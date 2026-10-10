user = {}

print("=====Login System=====")

while True:
    print("\n 1 : sing up")
    print("2 : Login")
    print("3 : Exit")

    choice = input("Enter your Choice: ")

    if choice == "1":
        username = input("Enter Username: ")
        password = input("Enter password: ")

        if username in user:
            print("User name Already exist")
        else:
            user[username] = password
            print("Account Created Successfully!")

    elif choice == "2":
        username = input("Enter Username: ")
        password = input("Enter password: ")

        if username in user and user[username] == password:
            print(f"Login successful!, Welcome {username}")
        else:
            print("Invalid combination of Username and password!")

    elif choice == "3":
        print("Thank you, sir")
        break
    else:
        print("Invalid choice")
