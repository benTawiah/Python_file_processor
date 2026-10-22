def get_product():
    product_name = input("Enter product name: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock quantity: "))
    product = {
        "name" : product_name,
        "price" : price,
        "stock" : stock
    }
    return product
    
def show_product(product):
    for key, value in product.items():
        if key == "price":
            print(f"{key.capitalize()} : {value:.2f}")
        elif key == "stock":
            print(f"{key.capitalize()} : {value} units")
        else:
             print(f"{key.capitalize()} : {value}")


#Accepting user input
product_data=get_product()


#Showing product
show_data = show_product(product_data)
print(show_data)
