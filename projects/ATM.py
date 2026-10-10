balance = 1000
correct_pin = "121345"
attempts = 0
max_attempts = 3

while attempts < max_attempts:

   try:
      pin = int(input("Enter your PIN: "))

      if pin == correct_pin:
         print("Allow access")
         break
      else:
         attempts += 1
         print("Incorrect PIN")
      
   except ValueError:
      print("Please enter a valid PIN.")

else:
    print("Too many incorrect attempts. Access denied.")
    exit()

while True:
    
   try:
      print("\n1: Check Balance")
      print("2: Withdraw Cash")
      print("3: Deposit Cash")
      print("4: Exit")

      choice = input("Enter your choice: ")

      if choice == "1":
         print(f"The amount in your account is: {balance}")

      elif choice == "2":
         withdraw = int(input("Enter amount you want to withdraw: "))

         if withdraw <= 0:
               print("Withdrawal amount must be greater than zero")

         elif withdraw > balance:
               print("Withdrawal amount can't be greater than your balance")

         else:
               balance -= withdraw
               print(f"Cash {withdraw} withdrawn successfully")

      elif choice == "3":
         deposit = int(input("Enter amount you want to deposit: "))

         if deposit < 0:
               print("Deposit amount can't be negative")

         elif deposit == 0:
               print("Deposit amount can't be zero")

         else:
               balance += deposit
               print(f"{deposit} deposited successfully")

      elif choice == "4":
         print("Thank you, sir! Have a nice day.")
         break

      else:
         print("Invalid choice")

   except ValueError:
       print("Please enter a valid number.")
      
      
