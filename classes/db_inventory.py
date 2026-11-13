import sqlite3

from product import Product

class DbInventory:
    def __init__(self, filename):
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS product(id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, price REAL CHECK(price >=0), stock INTEGER CHECK(stock>=0))")
        self.connection.commit()
        
    def add(self, name, price, stock):
        try:
            self.cursor.execute("INSERT INTO product(name, price, stock ) VALUES (?,?,?)", (name, price, stock))
        except sqlite3.IntegrityError as error:
            raise ValueError(f"Invalid inputs. {error}")
        self.connection.commit()
        
    def find(self, name):
        self.cursor.execute("SELECT * FROM product WHERE name = ?", (name,))
        row = self.cursor.fetchone()

        if row is None:
            return row
        return Product(row[1], row[2], row[3])
    
    def remove(self, name):
        self.cursor.execute("DELETE FROM product WHERE name =?", (name,))
        if self.cursor.rowcount == 0:
            raise ValueError("Product not found")
        self.connection.commit()
        
    def show_all(self):
        self.cursor.execute("SELECT * FROM product")
        for row in self.cursor.fetchall():
            product = Product(row[1], row[2], row[3])
            product.show_method()
    
    def sell(self, name,quantity):
        if quantity <=0:
            raise ValueError("can't be 0 or negative")
        self.cursor.execute("UPDATE product SET stock = stock - ?  WHERE name =? AND stock >= ?", (quantity,name, quantity))
        if self.cursor.rowcount == 0:
            if self.find(name) is None:
                raise ValueError("Product not found")
            raise ValueError("Not enough stock")
        self.connection.commit()
        
        
            


       
        
        
        
               




db = DbInventory("test_shop.db")
db.add("Pen", 2.2, 9)
db.add("Notebook", 5.6, 7)

found = db.find("Pen")

#db.sell("Pen", 1000)
db.sell("Pen", -5)

# if found is None:
#     print("Not found")
# else:
#found.show_method()


db.cursor.execute("SELECT * FROM product")
print(db.cursor.fetchall())




db.show_all()


        