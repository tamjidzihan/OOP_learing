from re import I
from turtle import st


class Item:
    '''
    Product Price calculator
    '''
    def __init__(self,name:str, price:float,quantity=0) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return  print(self.price * self.quantity)

item1 = Item('Phone',300,4)
item1.calculate_total_price()
