class Inventory:
    def __init__(self):
        self.product_collect =[]
    
    def add(self,product):
        self.product_collect.append(product)
        

p1 = Inventory()

p1.add("cook")
p1.add("Pen")

