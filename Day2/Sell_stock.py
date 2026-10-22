product ={
    "name": "Water bottle", 
    "price": 4.00, 
    "stock": 12
}

bottles_arrived = int(input("Enter the number of arrived bottles: "))
product['stock'] += bottles_arrived

customer_request = int(input("How many bottle would you like to buy: "))

customer = product['price'] * customer_request
if customer_request > 1 and customer_request < product['stock']:
    purchase= product['stock'] - customer_request
    product['stock'] = purchase
    
    print(f"purchased cost is {customer} and remaining stock is {product['stock']}")
else:
    print("The requested quantity has to be positive and customer reuest cannot exceed stock")
    
print(product)




    