product ={
    "product name": "NoteBook", 
    "price": 3.50, 
    "stock": 20
}

#function takes dictionary as argument
def calculate_stock_value(arg_name):
    stock_value = arg_name['price'] * arg_name['stock']
    return stock_value

#function creating dictionary
def create_product(name,price,stock):
    return {
        "name": name,
        "price": price,
        "stock": stock
    }
    
product = create_product("Iphone", 3.50, 5)
print(product)

# total_value = calculate_stock_value(product)
# print(f"The total value is {total_value}")