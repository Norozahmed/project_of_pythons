# Creating simple ATM 

accounts = {
    "1234567890": {"pin": "1234", "balance": 10000},
    "9876543210": {"pin": "5678", "balance": 15000}    
}

account_number = input('Enter your account number: ')
if account_number in accounts:
    pin = input("Enter you PIN: ")
    if pin == accounts[account_number]["pin"]:
        print("Login succesful!")
        # Now show the menu
        while True:  # Loop to keep the menu running until the user exits
              menu = input("""
Hey, Welcome to my ATM

1. Enter 1 for Pin change
2. Enter 2 for Balance check
3. Enter 3 for Withdraw
4. Enter 4 for Deposit 
5. Enter 5 for exit 
""")

              if menu == "1":
                  print("Pin Change functionality will go here.")  # Placeholder
              elif menu == "2":
                  print("Balance check functionality will go here.")  # Placeholder
              elif menu == "3":
                  print("Withdraw functionality will go here.")  # Placeholder
              elif menu == "4":
                  print("Deposit functionality will go here.")  # Placeholder
              elif menu == "5":
                  print("Thank you for using our ATM. Goodbye!")
                  break  # Exit the loop and end the program
              else:
                  print("Invalid input. Please enter a number between 1 and 5.")
        
    else:
        print("Incorrect PIN.")
else:
    print("Account not found.")

