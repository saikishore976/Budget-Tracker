import pandas as pd
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        # Create an empty DataFrame to store expenses
        self.expenses = pd.DataFrame(columns=["Date", "Category", "Description", "Amount"])

    def add_expense(self, date, category, description, amount):
        new_expense = {
            "Date": date,
            "Category": category,
            "Description": description,
            "Amount": amount,
        }
        self.expenses = pd.concat([self.expenses, pd.DataFrame([new_expense])], ignore_index=True)
        print("Expense added successfully!")

    def view_expenses(self):
        if self.expenses.empty:
            print("No expenses recorded.")
        else:
            print(self.expenses)

    def calculate_total(self):
        total = self.expenses["Amount"].sum()
        print(f"Total Expenses: ${total:.2f}")

    def save_to_csv(self, filename="expenses.csv"):
        self.expenses.to_csv(filename, index=False)
        print(f"Expenses saved to {filename}")

    def load_from_csv(self, filename="expenses.csv"):
        try:
            self.expenses = pd.read_csv(filename)
            print(f"Expenses loaded from {filename}")
        except FileNotFoundError:
            print("No file found. Starting with an empty tracker.")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add an Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Expenses")
        print("4. Save Expenses to CSV")
        print("5. Load Expenses from CSV")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category (e.g., Food, Transport): ")
            description = input("Enter a description: ")
            amount = float(input("Enter the amount: "))
            tracker.add_expense(date, category, description, amount)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.calculate_total()

        elif choice == "4":
            tracker.save_to_csv()

        elif choice == "5":
            tracker.load_from_csv()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
