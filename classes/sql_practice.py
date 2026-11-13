import sqlite3

connection = sqlite3.connect("shop.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS product(id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, price REAL CHECK (price >=0) , stock INTEGER CHECK(stock >=0))")
try:
    cursor.execute("INSERT INTO product(name, price, stock) VALUES (?,?,?)" ,('Notebook', 5.6, 7))
except sqlite3.IntegrityError as error:
    print(f"Cannot have duplicate. {error}")

try:
    cursor.execute("INSERT INTO product(name, price, stock) VALUES (?,?,?)" ,('Calculator', 7.8, 4))
except sqlite3.IntegrityError as error:
    print(f"Invalid value. Price cannot be less than 0.{error} ")
try:
    cursor.execute("INSERT INTO product (name, price, stock) VALUES (?,?,?)", ('Pen', 2.2, 9))
except sqlite3.IntegrityError as error:
    print(f"Invalid value. Stock cannot be less than 0.{error} ")
    





#cursor.execute("UPDATE product SET stock = stock - 2 WHERE name='Notebook'")
#cursor.execute("DELETE FROM product WHERE name = 'Pen'")
cursor.execute("SELECT * FROM product WHERE name= ? ", ("Notebook",))

connection.commit()
print(cursor.fetchall())

connection.close()