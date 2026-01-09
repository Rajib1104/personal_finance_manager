# src/reports.py

def category_summary(expenses):
    summary = {}

    for expense in expenses:
        if expense.category in summary:
            summary[expense.category] += expense.amount
        else:
            summary[expense.category] = expense.amount

    return summary


def total_expense(expenses):
    total = 0
    for expense in expenses:
        total += expense.amount
    return total
