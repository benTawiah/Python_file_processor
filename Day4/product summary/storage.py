import json
def save_product_into_file(product):
    with open('products.json',"w", encoding="utf-8") as file:
        json.dump(product,file, indent=4, ensure_ascii=False)
        
def load_product_data():
    with open('products.json', 'r', encoding="utf-8" ) as file:
        product =json.load(file)
    return product