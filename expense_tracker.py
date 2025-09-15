import json
from datetime import datetime

FILE_NAME = "expenses.json"

# Load expenses
def load_expenses():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save expenses
def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)

# Add expense
def add_expense(date, amount, category, description):
    expenses = load_expenses()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses.append(expense)
    save_expenses(expenses)

# Delete expense by index
def delete_expense(index):
    expenses = load_expenses()
    if 0 <= index < len(expenses):
        expenses.pop(index)
        save_expenses(expenses)

# Get all expenses
def get_expenses():
    return load_expenses()

# Summary
def get_summary():
    expenses = load_expenses()
    total = sum(exp["amount"] for exp in expenses)
    category_totals = {}
    for exp in expenses:
        category_totals[exp["category"]] = category_totals.get(exp["category"], 0) + exp["amount"]
    return total, category_totals
