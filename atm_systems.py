accounts = {
    "1001": {
        "name": "Vasu",
        "pin": "1234",
        "balance": 5000
    },

    "1002": {
        "name": "Rahul",
        "pin": "5678",
        "balance": 10000
    },

    "1003": {
        "name": "karthik",
        "pin": "4321",
        "balance": 7500
    }
}


def check_balance(account):
    print(f"\nCurrent Balance: ₹{accounts[account]['balance']}")


def deposit(account):

    try:
        amount = float(input("Enter deposit amount: ₹"))

        if amount <= 0:
            print("Please enter a valid amount.")

        else:
            accounts[account]["balance"] += amount
            print(f"₹{amount} deposited successfully.")

    except ValueError:
        print("Invalid input. Please enter numbers only.")


def withdraw(account):

    try:
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Please enter a valid amount.")

        elif amount > accounts[account]["balance"]:
            print("Insufficient balance.")

        else:
            accounts[account]["balance"] -= amount
            print(f"₹{amount} withdrawn successfully.")

    except ValueError:
        print("Invalid input. Please enter numbers only.")


print("====== ATM LOGIN ======")

account_number = input("Enter Account Number: ")
pin = input("Enter 4-digit PIN: ")

if account_number in accounts and accounts[account_number]["pin"] == pin:

    print("\nLogin Successful!")

    while True:

        print("\n====== ATM MENU ======")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(account_number)

        elif choice == "2":
            deposit(account_number)

        elif choice == "3":
            withdraw(account_number)

        elif choice == "4":
            print("Thank you for usi10ng the ATM.")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Invalid Account Number or PIN.")