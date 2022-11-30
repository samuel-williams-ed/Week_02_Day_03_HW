class Drinks():
    def __init__(self, input_name, input_price, input_strength, input_stock):
        self.name = input_name
        self.price = input_price
        self.strength = input_strength #int
        self.stock = input_stock

    #Methods:
    def reduce_stock(self):
        self.stock -= 1
