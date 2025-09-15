import streamlit as st
import pandas as pd
from expense_tracker import add_expense, get_expenses, get_summary, delete_expense

st.set_page_config(page_title="💸 Expense Tracker", layout="centered")

st.title("💸 Expense Tracker")

menu = ["Add Expense", "View Expenses", "Summary", "Delete Expense"]
choice = st.sidebar.radio("Menu", menu)

# Add expense
if choice == "Add Expense":
    st.subheader("➕ Add a New Expense")
    date = st.date_input("Date")
    amount = st.number_input("Amount (Rs)", min_value=0.0, format="%.2f")
    category = st.selectbox("Category", ["Food", "Transport", "Bills", "Shopping", "Other"])
    description = st.text_input("Description")

    if st.button("Add Expense"):
        add_expense(str(date), amount, category, description)
        st.success("✅ Expense Added Successfully!")

# View expenses
elif choice == "View Expenses":
    st.subheader("📒 All Expenses")
    expenses = get_expenses()

    if expenses:
        df = pd.DataFrame(expenses)
        st.dataframe(df)
    else:
        st.info("⚠️ No expenses recorded yet.")

# Summary
elif choice == "Summary":
    st.subheader("📊 Expense Summary")
    total, category_totals = get_summary()
    st.write(f"💰 **Total Expenses:** Rs {total}")

    if category_totals:
        df = pd.DataFrame(list(category_totals.items()), columns=["Category", "Amount"])
        st.bar_chart(df.set_index("Category"))

# Delete expense
elif choice == "Delete Expense":
    st.subheader("🗑️ Delete an Expense")
    expenses = get_expenses()

    if expenses:
        df = pd.DataFrame(expenses)
        st.dataframe(df)

        index = st.number_input("Enter the index of the expense to delete (starting from 0)", min_value=0, max_value=len(expenses)-1)
        if st.button("Delete Expense"):
            delete_expense(index)
            st.success("✅ Expense Deleted Successfully!")
    else:
        st.info("⚠️ No expenses to delete.")
