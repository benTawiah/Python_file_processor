product ={
    "name": "Notebook", 
    "price": 3.50, 
    "stock": 20
}

#updating dictionary with new key and value 
product["category"] = "Stationary"

#changing value of key
product["price"] = 4

print(product)

#removing elements
product.pop('category')

print(product)