product =[{"name": "Notebook", "price": 3.50, "stock": 20},
          {"name": "Pen", "price": 1.20, "stock": 50},
          {"name": "Folder", "price": 2.80, "stock": 15}
          ]

# for  element in product:
#     print(element)
    
# for  element in product:
#     print(element['name'],":$", element['price'])

print(product[0]["price"])
print(product[2]["name"])

#adding new dictionary to list
new_product={
    "name" : "Pencil",
    "price": 0.8,
    "stock": 30
        
}

product.append(new_product)

for  element in product:
    print(element)
    
