import sqlite3
from product import Product


class DbInventory:
    def __init__(self, filename):
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS product("
            "id INTEGER PRIMARY KEY, "
            "name TEXT NOT NULL UNIQUE COLLATE NOCASE CHECK(length(trim(name)) > 0), "
            "price REAL CHECK(price >= 0), "
            "stock INTEGER CHECK(stock >= 0))"
        )
        self.connection.commit()

    def add(self, name, price, stock):
        name = name.strip()
        if not name:
            raise ValueError("Name cannot be empty")
        try:
            self.cursor.execute(
                "INSERT INTO product(name, price, stock) VALUES (?, ?, ?)",
                (name, price, stock),
            )
        except sqlite3.IntegrityError as error:
            raise ValueError(f"Invalid inputs. {error}") from error
        self.connection.commit()

    def find(self, name):
        self.cursor.execute(
            "SELECT name, price, stock FROM product WHERE name = ?", (name,)
        )
        row = self.cursor.fetchone()
        if row is None:
            return None
        return Product(*row)

    def remove(self, name):
        self.cursor.execute("DELETE FROM product WHERE name = ?", (name,))
        if self.cursor.rowcount == 0:
            raise ValueError("Product not found")
        self.connection.commit()

    def show_all(self):
        self.cursor.execute("SELECT name, price, stock FROM product")
        return [Product(*row) for row in self.cursor.fetchall()]

    def sell(self, name, quantity):
        if quantity <= 0:
            raise ValueError("Quantity cannot be 0 or negative")
        self.cursor.execute(
            "UPDATE product SET stock = stock - ? WHERE name = ? AND stock >= ?",
            (quantity, name, quantity),
        )
        if self.cursor.rowcount == 0:
            if self.find(name) is None:
                raise ValueError("Product not found")
            raise ValueError("Not enough stock")
        self.connection.commit()

    def close(self):
        self.connection.close()