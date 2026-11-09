import json
class Product:
    def __init__(self, name, price, stock):
        
        if price < 0:
            raise ValueError("Price cannot be negative.")
    
        if stock < 0:
            raise ValueError("Stock cannot be negative.")
        
              
        self.name = name
        self.price = price
        self.stock = stock
        
    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }
        
            
    def show_method(self):
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock} units")
    
        
    def sell(self, quantity):
       
        if quantity <= 0:
            raise ValueError("Quantity cannot be 0 or negative")
        
        if quantity > self.stock:
            print("Quantity is more than the current stock")
        else:
            self.stock -= quantity
        
class Inventory:
    def __init__(self):
        self.product_collect =[]
        
    def add(self,name, price, stock):
        if self.find(name) is not None:
            raise ValueError("Product already exists.")
        product = Product(name, price, stock)
        self.product_collect.append(product)
        
    def find(self, name):
        for product in self.product_collect:
            if product.name == name:
                return product
        return None
    
    def remove(self, name):
        product = self.find(name)
        if product is None:
            print ("Product not found")
        else:
            self.product_collect.remove(product)
            
    def save(self, filename):
        data = []
        for product in self.product_collect:
            data.append(product.to_dict())
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
            
    def load(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("No saved file found, starting empty")
            return

        for item in data:
            self.add(item["name"], item["price"], item["stock"])
            
		
        
    
    def show_all(self):
        for product in self.product_collect:
            product.show_method()
        
        
        
        
        
