expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        expense = input("Enter an expense: ")
        amount = float(input("Enter the amount: ₹"))

        expenses.append([expense, amount])

        print("Expense added successfully! ✅")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses added yet.")
        else:
            print("\nYour Expenses:")

            for item in expenses:
                print(item[0], "₹", item[1])

    elif choice == "3":
        total = sum(item[1] for item in expenses)
        print("Total spending: ₹", total)

    elif choice == "4":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice!")
