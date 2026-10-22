customer = {
    "name": "Alex",
    "email": "alexa@gmail.com",
    "orders": 3
}

# print(f"{customer['name']} made {customer['orders']} orders")

# if 'email' in customer:
#     print(customer["email"])

print(customer.get("phone","Not provided"))# used to enter key that might not exist in the dictionary