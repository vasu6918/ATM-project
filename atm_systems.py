print("      ATM BANKING SYSTEM")

name = input("Enter account holder name: ")
balance = 5000

while True:

    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print(f"\nCurrent Balance: ₹{balance}")

    elif choice == "2":
        amount = int(input("Enter amount to deposit: ₹"))
        balance += amount
        print(f"₹{amount} deposited successfully.")

    elif choice == "3":
        amount = int(input("Enter amount to withdraw: ₹"))

        if amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    elif choice == "4":
        print(f"\nThank you, {name}!")
        break

    else:
        print("Invalid choice.")