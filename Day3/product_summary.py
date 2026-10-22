import json
def get_product():
    #get data from user
    product_name = input("Enter product name: ")
    while True:
        try:
            price = float(input("Enter price: "))
            if price < 0:
                print("Price cannot be negative")
            else:
                break
        except ValueError:
            print("Invalid price. Please enter a number such us 3.5")
    while True:
        try:
            stock = int(input("Enter stock quantity: "))
            if stock < 0:
                print("Stock cannot be negative")
            else:
                break
        except ValueError:
            print("Invalid Stock. Please enter a number.")
                
           
    #store data in dictionary
    product = {
        "name" : product_name,
        "price" : price,
        "stock" : stock
            }
    return product

    #collecting dictionary of product and storing into list
def collect_products():
    list_of_products =[]
    answer = "yes"
    while True:
        
        if  answer.lower().strip() == "yes" :
             product = get_product()
             list_of_products.append(product) 
        elif answer.lower().strip() == "no":
            break
        
        else:
            print("Invalid response. enter yes/no")
        
        answer = input("Add another product? yes/no:")
    return list_of_products

#function to display product summary
def show_product(product):
    for key, value in product.items():
        if key == "price":
            print(f"{key.capitalize()} : {value:.2f}")
        elif key == "stock":
            print(f"{key.capitalize()} : {value} units")
        else:
            print(f"{key.capitalize()} : {value.capitalize()}")


# Accepting user input
product_data = collect_products()

# Showing all products
for product in product_data:
    print("\n--- Product ---")
    show_product(product)
