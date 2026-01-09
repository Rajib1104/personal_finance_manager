# main.py
# Connected to all

from src.expense import Expense
from src.file_manager import load_expenses, save_expense
from src.menu import show_menu
from src.utils import validate_amount, validate_date
from src.reports import category_summary, total_expense

def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            amount = input("Amount: ")
            if not validate_amount(amount):
                print("Invalid amount")
                continue

            category = input("Category: ")
            date = input("Date (YYYY-MM-DD): ")
            if not validate_date(date):
                print("Invalid date")
                continue

            desc = input("Description: ")
            exp = Expense(amount, category, date, desc)
            save_expense(exp)
            expenses.append(exp)
            print("Expense added successfully!")

        elif choice == "2":
            for e in expenses:
                print(e)

        elif choice == "3":
            summary = category_summary(expenses)
            for k, v in summary.items():
                print(k, "=> ₹", v)
            print("Total:", total_expense(expenses))

        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
