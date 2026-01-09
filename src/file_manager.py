# src/file_manager.py

import csv
import os
from src.expense import Expense

FILE_NAME = "data/expenses.csv"


def load_expenses():
    expenses = []

    if not os.path.exists(FILE_NAME):
        return expenses

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) != 4:
                continue
            date, category, amount, description = row
            expenses.append(Expense(amount, category, date, description))

    return expenses


def save_expense(expense):
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(expense.to_list())
