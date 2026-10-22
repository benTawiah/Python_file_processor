sales ={
    "Monday": 12,
    "Tuesday" :8,
    "Wednesday":15,
    "Thursday": 18,
    "Friday": 10
}

# for day in sales:
#     print(day)
    
for day, product in sales.items():
    print(day,":",product)