class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        self.last_transaction = price * quantity
        self.total += self.last_transaction
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${ int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0

# Example usage:

# Creating an instance of CashRegister
register = CashRegister(discount=20)

# Adding items
register.add_item("apple", 1.00, 3)
register.add_item("banana", 0.50, 2)

# Applying discount
register.apply_discount()  # Should apply the discount and print the new total

# Voiding the last transaction
register.void_last_transaction()
print(register.total)  # Should print the total after voiding the last transaction
