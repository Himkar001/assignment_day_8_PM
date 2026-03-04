# Paytm Transaction Analyzer

transactions = []

print("Enter transactions. Type 'done' to finish.\n")

# While loop to collect transactions
while True:

    user_input = input("Enter amount (or 'done'): ")

    if user_input.lower() == "done":
        break

    amount = float(user_input)

    t_type = input("Type (credit/debit): ").lower()

    transaction = {
        "amount": amount,
        "type": t_type
    }

    transactions.append(transaction)

    # High value transaction flag
    if amount > 10000:
        print("⚠ High value transaction detected!\n")


total_credit = 0
total_debit = 0
highest_transaction = 0

# Analyze transactions
for t in transactions:

    amount = t["amount"]

    if t["type"] == "credit":
        total_credit += amount
    else:
        total_debit += amount

    if amount > highest_transaction:
        highest_transaction = amount


transaction_count = len(transactions)

if transaction_count > 0:
    average = (total_credit + total_debit) / transaction_count
else:
    average = 0


# Bar chart of last 10 transactions
print("\nLast 10 Transactions Chart")

last_transactions = transactions[-10:]

for t in last_transactions:

    stars = int(t["amount"] / 1000)

    for i in range(stars):
        print("*", end="")

    print()


# Summary
print("\nTransaction Summary")

print("Total transactions:", transaction_count)
print("Total credits:", total_credit)
print("Total debits:", total_debit)
print("Net balance:", total_credit - total_debit)
print("Highest transaction:", highest_transaction)
print("Average amount:", average)