def get_people():
    people = input("Enter names of people, separated by commas: ").split(",")
    return [p.strip() for p in people if p.strip()]

def record_expenses(people):
    expenses = {person: 0 for person in people}
    while True:
        print("\nEnter expense (or 'done' to finish):")
        payer = input("Who paid? ")
        if payer.lower() == 'done':
            break
        if payer not in people:
            print("Person not in group, try again.")
            continue
        amount = input("Amount paid: ")
        try:
            amount = float(amount)
        except:
            print("Invalid amount, try again.")
            continue
        expenses[payer] += amount
    return expenses

def calculate_settlement(expenses):
    total = sum(expenses.values())
    n = len(expenses)
    fair_share = total / n
    print("\nTotal expenses: {:.2f}".format(total))
    print("Each owes: {:.2f}".format(fair_share))
    balances = {person: paid - fair_share for person, paid in expenses.items()}
    print("\nSettlements:")
    for person, balance in balances.items():
        if balance > 0:
            print(f"{person} should receive {balance:.2f}")
        elif balance < 0:
            print(f"{person} owes {-balance:.2f}")
        else:
            print(f"{person} is settled.")

def main():
    print("Welcome to Simple Expense Splitter")
    people = get_people()
    if not people:
        print("No people entered, exiting.")
        return
    expenses = record_expenses(people)
    calculate_settlement(expenses)

if __name__ == "__main__":
    main()
