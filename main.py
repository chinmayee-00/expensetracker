import json

class ExpenseTracker:
    def _init_(self):
        self.expenses = []
        self.budget = {}
        self.load_data()

    def add_expense(self, amount, category, description):
        """Add a new expense."""
        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }
        self.expenses.append(expense)
        self.save_data()
        print(f"Expense of {amount} added under {category}.")

    def set_budget(self, category, amount):
        """Set a budget for a specific category."""
        self.budget[category] = amount
        self.save_data()
        print(f"Budget of {amount} set for {category}.")

    def show_expenses(self):
        """Display all expenses."""
        if not self.expenses:
            print("No expenses recorded.")
            return

        print("\nYour Expenses:")
        for expense in self.expenses:
            print(f"Amount: {expense['amount']} | Category: {expense['category']} | Description: {expense['description']}")
        print()

    def show_budget_status(self):
        """Show the budget status for each category."""
        if not self.budget:
            print("No budgets set.")
            return

        print("\nYour Budget Status:")
        for category, budget_amount in self.budget.items():
            category_expenses = sum(expense['amount'] for expense in self.expenses if expense['category'] == category)
            remaining_budget = budget_amount - category_expenses
            status = "Under Budget" if remaining_budget >= 0 else "Over Budget"
            print(f"Category: {category} | Budget: {budget_amount} | Spent: {category_expenses} | Remaining: {remaining_budget} | Status: {status}")
        print()

    def save_data(self):
        """Save expenses and budget to a JSON file."""
        with open("expenses_data.json", "w") as file:
            json.dump({"expenses": self.expenses, "budget": self.budget}, file, indent=4)

    def load_data(self):
        """Load expenses and budget from a JSON file."""
        try:
            with open("expenses_data.json", "r") as file:
                data = json.load(file)
                self.expenses = data.get("expenses", [])
                self.budget = data.get("budget", {})
        except (FileNotFoundError, json.JSONDecodeError):
            self.expenses = []
            self.budget = {}

# Example Usage
if _name_ == "_main_":
    tracker = ExpenseTracker()

    while True:
        print("\n1. Add Expense\n2. Set Budget\n3. Show Expenses\n4. Show Budget Status\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category (e.g., Food, Transportation): ")
            description = input("Enter expense description: ")
            tracker.add_expense(amount, category, description)

        elif choice == "2":
            category = input("Enter category to set budget for: ")
            amount = float(input(f"Enter budget amount for {category}: "))
            tracker.set_budget(category, amount)

        elif choice == "3":
            tracker.show_expenses()

        elif choice == "4":
            tracker.show_budget_status()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
