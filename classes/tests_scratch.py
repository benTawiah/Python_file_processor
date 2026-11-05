import json
from product import Product, Inventory

prod = Product("Phone", 6.989, 7)
shop = Inventory()


shop.add("Notebook", 6.989, 7)
shop.add("Pen",  5.989, 9)
shop.add("calculator", 6.989, 7)
shop.add("Phone", 200.989, 7)

print(prod.to_dict())

print(f"The lenght of list after adding product: {len(shop.product_collect)}") 

shop.remove("Pen")
shop.remove("Cup")


print(f"The lenght of list after removing product: {len(shop.product_collect)}")    

shop.save("product.json")  

found = shop.find("Pen")
if found is None:
    print("Not found")
else:
    found.sell(2)
    

shop.load("product.json")
print("*" * 20)
shop.show_all()

shop3 = Inventory()
shop3.load("nothing.json")
print(len(shop3.product_collect))

shop2 = Inventory()
shop2.load("product.json")
#shop2.show_all()



   