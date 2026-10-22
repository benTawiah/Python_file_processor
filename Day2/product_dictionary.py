product_name = input("Enter product name: ")
price = float(input("Enter price: "))
stock_quantity = int(input("Enter stock quantity: "))

product ={
    "product name": product_name, 
    "price": price, 
    "stock quantity": stock_quantity
}

print("x" *20)
print("whole dictionary")
print("x" *20)
print (f"{product}\n")

print("x" *20)
print("Product Summary")
print("x" *20)
print(f"Name: {product['product name']}")
print(f"Price: {product['price']:.2f}")#convert to two decimal point
print(f"Stock: {product['stock quantity']} unit")

