from db_inventory import DbInventory


shop = DbInventory("shop.db")


while True:
    print("\n1. Add a product")
    print("2. Sell a product")
    print("3. Show all")
    print("4. Remove a product")
    print("5. Save and quit")
    
    choice = input("Choose an option: ")

    if choice == "3":
        for product in shop.show_all():
            product.show_method()

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
        try:
            quantity = int(input("Quantity to sell: "))
            shop.sell(name, quantity)
            shop.find(name).show_method()
        except ValueError as error:
            print(f"Could not sell: {error}")

    elif choice == "4":
        name = input("Product name: ")
        try:
            shop.remove(name)
            print(f"{name} removed")
        except ValueError as error:
            print(f"Could not remove: {error}")

    elif choice == "5":
        shop.close()
        print("Goodbye!")
        break
    





        