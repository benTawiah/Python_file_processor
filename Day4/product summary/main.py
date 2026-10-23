from product_function import collect_products, show_product
from storage import load_product_data, save_product_into_file

#load previously saved data
all_products = load_product_data()

#collect new products from the user
new_products = collect_products()

#add new products to existing list of products
all_products.extend(new_products)

#save the complete updateed list
save_product_into_file(all_products)



# Display product summary
for product in new_products:
    print("\n--- Product ---")
    show_product(product)

