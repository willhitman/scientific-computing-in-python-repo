class Category:
    
    def __init__(self, category):
        self.category = category
        self.ledger = []
    
    def __str__(self):
       print_out = f'{self.category:*^30}'
       for transaction in self.ledger:
           print_out += f"\n{transaction['description'][:23]:23}{transaction['amount']:>7.2f}"
       print_out += f"\nTotal: {self.get_balance():.2f}"
       return print_out


    def deposit(self, amount, description = ''):
        self.amount = amount
        self.description = description 

        self._add_to_ledger(self.amount, self.description)


    def withdraw(self, amount, description = ''):
        if  not self.check_funds(amount):
            return False
        else:
            self.amount = -1 * amount
            self.description = description 
            self._add_to_ledger(self.amount, self.description)

            return True
    
    def get_balance(self):
        _sum = 0
        for transaction in self.ledger:
            _sum += transaction['amount']
        return _sum

    def transfer(self, amount, category):

        if not self.check_funds(amount):
            return False
        else:
            self.description =  f'Transfer to {category.category}'
            self.withdraw(amount, self.description)
            category.deposit(amount, f'Transfer from {self.category}')
            return True 


    def check_funds(self, amount):
        if not amount <= self.get_balance():
            return False
        return True
    
    def _add_to_ledger(self, amount, description):
        self.ledger.append({'amount': amount, 'description':description})


def create_spend_chart(categories):
    # Step 1: Calculate the total spend for all categories
    total_spent = 0
    spent_per_category = []

    for category in categories:
        spent = 0
        for entry in category.ledger:
            if entry["amount"] < 0:  # Only include withdrawals (spending)
                spent += abs(entry["amount"])
        spent_per_category.append(spent)
        total_spent += spent
        
    percentages = [(spent / total_spent) * 100 for spent in spent_per_category]

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    -" + "---" * len(categories) + "\n"

    max_len = max([len(category.category) for category in categories])
    category_names = [category.category.ljust(max_len) for category in categories]

    for i in range(max_len):
        chart += "     "
        for name in category_names:
            chart += name[i] + "  "
        chart += "\n"

    return chart.rstrip("\n")



food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print(clothing)
clothing.withdraw(10,)

create_spend_chart([food,clothing])
