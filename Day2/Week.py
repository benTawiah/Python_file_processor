days =["Monday", "Tuesday", "Wednesday","Thursday", "Friday"]

sales={}

for day in days:
    quantity = int(input(f"How many items were sold on {day}: "))
    sales[day]= quantity
    
print("***Display***")
for day,quantity in sales.items():
    print(f"{day} : {quantity} sold")
    
total_sales = sum(sales.values())

print(f"the total sales was {total_sales}")

average_sale = total_sales /len(sales)
print(f"the average sales was {average_sale:.2f}")

for day, quantity in sales.items():
    if quantity > average_sale:
        print(f"{day} exceeded average sale, with sales of {quantity}")

highest_sales=0        
for day, quantity in sales.items():
    if quantity > highest_sales:
        highest_sales = quantity
        print(f"Highest sales quantity was {highest_sales} and it occured on {day}")
    
    