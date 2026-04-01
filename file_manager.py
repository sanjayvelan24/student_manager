import json

def load_expense(filename):
    try:
        with open(filename,"r")as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def save_expense(filename, expense_list):
    try:
        with open(filename, "w")as f:
            json.dump(expense_list, f)
            print("Saved succesfully")
    except Exception as e:
        print(f"Error is : {e}")

# r = save_expense("expense.json", [{"title": "Icecream", "amount" : 100, "category": "food"}])
# r=load_expense("expense.json")

# print(r)
    