product_name = input("Enter product name: ")
price = float(input("Enter price: "))
stock_quantity = int(input("Enter stock quantity: "))

product ={
    "product name": product_name, 
    "price": price, 
    "stock": stock_quantity
}


def calculate_stock_value(product):
    stock_value = product['price'] * product['stock']
    return stock_value


value = calculate_stock_value(product)
print(f"The total value in store is: {value}")
    
    
    
    
# print("x" *20)
# print("whole dictionary")
# print("x" *20)
# print (f"{product}\n")

# print("x" *20)
# print("Product Summary")
# print("x" *20)
# print(f"Name: {product['product name']}")
# print(f"Price: {product['price']:.2f}")#convert to two decimal point
# print(f"Stock: {product['stock quantity']} unit")

