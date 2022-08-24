class Item:
    pay_rate = 0.8
    all = []
    def __init__(self,name:str, price:float,quantity=0) -> None:
        
        assert price >=1, f"Price {price} is not greater then zero!"
        assert quantity >=1

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return  print(self.price * self.quantity)

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self) -> str:
        return f"Item('{self.name}','{self.price}','{self.quantity}')"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)