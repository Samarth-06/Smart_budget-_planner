# importing the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Define budget and categories
budget = float(input("Enter your monthly budget: ₹"))

cat = ['Rent', 'Groceries', 'Utilities', 'Transport', 'Entertainment', 'Education', 'Others']
exp = []

print("Enter expense in each category:")
for i in cat:
    x = float(input(f"{i}: ₹"))
    exp.append(x)

data = pd.DataFrame({
    'Category': cat,
    'Expense': exp
})

total = np.sum(data['Expense'])
left = budget - total
data['Percent'] = (data['Expense'] / budget) * 100
avg = budget / len(cat)
data['AboveAvg'] = data['Expense'] > avg

print("\nYour Expense Summary:")
print(data)
print("\nTotal Spent: ₹", total)
print("Remaining Budget: ₹", left)

# Using conditional statements
if left < 0:
    print("You have spent more than your budget 😓")
else:
    print("Nice! You are in your budget 😄")
    
# Pie chart of category-wise spending
plt.figure(figsize=(8, 8))
plt.pie(data['Expense'], labels=data['Category'], autopct='%1.1f%%')
plt.title("Where Your Money Went")
plt.show()

# Bar chart of expenses
plt.figure(figsize=(10, 5))
plt.bar(data['Category'], data['Expense'], color='orange')
plt.axhline(avg, color='red', linestyle='--', label='Average Limit')
plt.title("Spending in Each Category")
plt.ylabel("Expense (₹)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
