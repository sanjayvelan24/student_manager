from expense import expense
from file_manager import load_expense, save_expense

filename = "expense.json"
expenses = load_expense(filename)

while True:
    print("1. Add the expenses")
    print("2.View all the expenses")
    print("3. total amount of all the expenses")
    print("4. view expenses using input category")
    print("5. Exit")

    try:
        choice = int(input("enter the choice..."))
    except ValueError:
        print("enter the right choice")
        continue

    if choice == 1:
        try:
            amount = int(input("enter the amount"))
        except ValueError:
            print("Enter the valid amount in numeric")
            continue

        title = input("enter the title ")
        category = input("enter the category")
        e= expense(title, amount, category)
        expenses.append(e.to_dict())
        save_expense(filename, expenses)
    elif choice == 2:
        for d in expenses:
            print(d["title"],d["amount"],d["category"])
    elif choice == 3:
        total = 0
        for d in expenses:
            total += d["amount"]
        print("Total of the amount: ", total)
    elif choice == 4:
        cat = input("enter the category to view the expenses")
        for d in expenses:
            if d["category"].lower() == cat.lower():
                print(d["title"], d["amount"], d["category"])
    elif choice == 5:
        break
    


