from product import Inventory


shop = Inventory()
shop.load("product.json")

while True:
    print("\n1. Add a product")
    print("2. Sell a product")
    print("3. Show all")
    print("4. Remove a product")
    print("5. Save and quit")
    
    choice = input("Choose an option: ")

    if choice == "3":
        shop.show_all()
    
    elif choice == "1":
            name = input("Product name: ")
            try:
                price = float(input("Price: "))
                stock = int(input("Stock: "))
                shop.add(name, price, stock)
                print("Product added")
            except ValueError as error:
                print(f"Could not add product. {error}")
    elif choice == "2":
        name = input("Product name: ")
        product = shop.find(name)
        if product is None:
            print("Product not found")
        else:
            try:
                quantity = int(input("Quantity to sell: "))
                product.sell(quantity)
                product.show_method()
            except ValueError as error:
                print(f"Could not sell: {error}")
        
    elif choice == "4":
        name = input("Product name: ")
        product= shop.find(name)
        if product is None:
            print("Product not found")
        else:
            product = shop.remove(name)
            print(f"{name} removed")
           
                         
    elif choice == "5":
        shop.save("product.json")
        print("Saved. Goodbye!")
        break
    
    else:
        print("That option is not ready yet, or it is invalid.")
    


