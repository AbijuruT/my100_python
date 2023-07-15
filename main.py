class Item:
    # Class attributes
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=1) -> None:
        # Validating inputs
        assert price >= 500, f"Price can't be bellow 500"
        assert quantity >= 1, f"Quantity can't be bellow 1"
        # Assignment of self obj
        self.name = name
        self.price = price
        self.quantity = quantity
        #Action to execute
        Item.all.append(self)

    def calculating_total(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self) -> str:
        #Adding the representation of objects
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 600, 6)
item2 = Item("Laptop", 2000, 3)
item3 = Item("Keyboard", 1500, 2)
item4 = Item("Screen", 1400, 1)
item5 = Item("Cable", 700, 2)

print(Item.all)
