class Shirt:

    def __init__(self, color, size, style, price):
        self.color = color
        self.color = color
        self.size = size
        self.price = price

    def change_price(self, price):
        self.price = price
        
    def discount(self, discount):
        return self.price * (1 - discount)