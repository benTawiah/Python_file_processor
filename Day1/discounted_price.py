def discounted_price(original_price, discount_percent):
    discount_amount = original_price * (discount_percent / 100)
    final_price = original_price - discount_amount
    return final_price

origin_price = float(input("Enter the original price: "))
disc_percent = float(input("Enter the discount percentage: "))

final_price = discounted_price(origin_price, disc_percent)

print(f"The final price $ {final_price}")