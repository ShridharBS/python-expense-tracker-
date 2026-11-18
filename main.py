import csv
import os
def show_menu():
    print("===============================")
    print("Welcome to Expense Tracker")
    print("===============================")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Search by Category")
    print("5. Category Summary")
    print("6. Exit")

expenses = []

def load_expenses():
    try:
        with open("expenses.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            for expense in reader:
                expenses.append({
                    "amount": float(expense["amount"]),
                    "category": expense["category"],
                    "date": expense["date"]
                })

    except FileNotFoundError:
        print("No previous expenses found.")


def category_summary():
    summary = {}

    try:
        with open("expenses.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            for expense in reader:
                category = expense["category"]
                amount = float(expense["amount"])

                if category in summary:
                    summary[category] += amount
                else:
                    summary[category] = amount

        print("\n--- CATEGORY SUMMARY ---")

        if not summary:
            print("No expenses available.")
        else:
            for category, total in summary.items():
                print(f"{category}: ₹{total:.2f}")

    except FileNotFoundError:
        print("No expenses found.")



def add_expense():
    print("Step 1: Function started")

    try:
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return
    category = input("Enter category: ")
    date = input("Enter date (DD-MM-YYYY): ")

    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }

    print("Step 2: Expense details collected")

    with open("expenses.csv", "a", newline="") as file:
        print("Step 3: CSV file opened")

        writer = csv.DictWriter(
            file,
            fieldnames=["amount", "category", "date"]
        )

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(expense)

        print("Step 4: Expense written to CSV")

    print("Step 5: File closed")
    print("Expense added successfully!")

def view_expenses():
    try:
        with open("expenses.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            print("\n--- ALL EXPENSES ---")

            for expense in reader:
                print(
                    f"Amount: ₹{expense['amount']} | "
                    f"Category: {expense['category']} | "
                    f"Date: {expense['date']}"
                )

    except FileNotFoundError:
        print("No expenses found.")

def view_total():
    total = 0

    try:
        with open("expenses.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            for expense in reader:
                total += float(expense["amount"])

        print(f"\nTotal Expenses: ₹{total:.2f}")

    except FileNotFoundError:
        print("No expenses found.")  

def search_category():
    search = input("Enter category to search: ").strip().lower()

    found = False

    try:
        with open("expenses.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            for expense in reader:
                if expense["category"].strip().lower() == search:
                    print(
                        f"Amount: ₹{expense['amount']} | "
                        f"Category: {expense['category']} | "
                        f"Date: {expense['date']}"
                    )
                    found = True

        if not found:
            print("No matching expenses found.")

    except FileNotFoundError:
        print("No expenses found.")       


while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        view_total()

    elif choice == "4":
        search_category()

    elif choice == "5":
        category_summary()

    elif choice == "6":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Try again.")



