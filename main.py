import csv

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self,name:str, price:float,quantity=0) -> None:
        
        assert price >=1, f"Price {price} is not greater then zero!"
        assert quantity >=1

        self.name = name
        self.price = price
        self.quantity = quantity
        
        price('hi')
        Item.all.append(self)

    def calculate_total_price(self):
        return  self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv','r')as file:
            reader = csv.DictReader(file)
            items  = list(reader)
            
            
        for i in items:
            Item(
                name = i.get('name'),
                price=float(i.get('price')),
                quantity=float(i.get('quantity'))
            )

        
    @staticmethod
    def is_int(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False


    def __repr__(self) -> str:
        return f"Item('{self.name}','{self.price}','{self.quantity}')"

