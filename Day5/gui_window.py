import tkinter as tk
import tkinter as ttk
products=[]
def get_product():
    product_name = name_entry.get().strip()
    product_price = price_entry.get().strip()
    product_stock = stock_entry.get().strip()
    
    product={
        "name": product_name,
        "price" : product_price,
        "stock": product_stock
    }
    return product


def add_products():
    product = get_product()
    products.append(product)
    
    name_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    stock_entry.delete(0, tk.END)
    
    name_entry.focus_set()
    
def show_products(product_dictionary):
    summary = "Product Summary"
    for key, value in product_dictionary():
        if key == "price":
            summary + f"{key.capitalize()} : {value:.2f}\n"
        elif key == "stock":
            summary + f"{key.capitalize()} : {value} units\n"
        else:
            summary + f"{key.capitalize()} : {value.capitalize()}"
    return summary
    

window = tk.Tk()
window.title("Labels")

heading = tk.Label(window, text="Welcome to our application")
heading.grid(column=0, row=0,  padx=5, pady=5)#creating padding for heading

name_label = ttk.Label(window, text="Product name: ")
name_label.grid(column=0, row=1,sticky="e",  padx=20, pady=20)

name_entry= ttk.Entry(window, width=30 )
name_entry.grid(column=1, row=1, sticky="w",  padx=20, pady=20)

price_label = ttk.Label(window, text="Product price: ")
price_label.grid(column=0, row=2,sticky="e", padx=20, pady=20)

price_entry= ttk.Entry(window, width=30 )
price_entry.grid(column=1, row=2, sticky="w",  padx=20, pady=20)

stock_label = ttk.Label(window, text="Stock Quantity: ")
stock_label.grid(column=0, row=3, sticky="e",  padx=20, pady=20)

stock_entry= ttk.Entry(window, width=30 )
stock_entry.grid(column=1, row=3, sticky="w",  padx=20, pady=20)

add_button = tk.Button(window, text="Add product", command=add_products)
add_button.grid(column=0, row=4,columnspan=2,  pady=10, sticky="e")


#creating label for feedback
message_label = ttk.Label(window,text="")
message_label.grid(column=0, row=5,columnspan=2,  pady=10, sticky="w")

#creating button to show feedback
show_button = tk.Button(window, text="Show Product", command=show_products)
show_button.grid(column=0, row=6,columnspan=2,  pady=10, sticky="e")

product_display = ttk.Text(window, width=60,height=12,wrap="word", state="disabled" )
product_display.grid(column=0, row=7,columnspan=2, padx=10, pady=10, sticky="w")




window.geometry("800x600")

window.mainloop()