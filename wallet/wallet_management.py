import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np

# Define your fixed monthly values
phone_bill = 38
miscellaneous = 20
lunch_expense_per_day = 7
saving_goal = 700

def calculate_remaining_balance(current_money, current_day, total_days):
    # Calculate the remaining money after subtracting the fixed monthly expenses and saving goal
    remaining_money = current_money - saving_goal

    # Total spending for the rest of the month
    total_spending_rest_of_month = lunch_expense_per_day * (total_days - current_day + 1)

    # Remaining balance at the end of the month after spending for the rest of the month
    remaining_balance = remaining_money - total_spending_rest_of_month

    return remaining_balance

def calculate_money_evolution(current_money, current_day, total_days):
    remaining_balances = []
    for day in range(current_day, total_days+1):
        remaining_balance = calculate_remaining_balance(current_money, day, total_days)
        remaining_balances.append(remaining_balance)
        current_money -= (lunch_expense_per_day + remaining_balance / (total_days - day + 1))

    return pd.DataFrame({"Day": np.arange(current_day, total_days+1), "Remaining Balance": remaining_balances})

st.title('Money Management System')

# User inputs the current money left
current_money = st.number_input("Enter your current total money:")

# Get today's date
now = datetime.now()
current_day = now.day

# For simplicity, we assume every month has 30 days
total_days = 30

remaining_balance = None  # Default value for remaining_balance

if st.button('Submit'):
    remaining_balance = calculate_remaining_balance(current_money, current_day, total_days)

    # Display pile of money
    money_bags = "💰" * int(remaining_balance / 100)  # One money bag emoji for each 100 euros
    st.write(money_bags)

    # Display money evolution chart
    money_evolution_df = calculate_money_evolution(current_money, current_day, total_days)
    st.line_chart(money_evolution_df.set_index("Day"))

if remaining_balance is not None:
    st.write(f"Your predicted remaining balance at the end of the month is: €{remaining_balance:.2f}")
