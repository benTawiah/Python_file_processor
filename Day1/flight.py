def check_suitcase(weight, limit):
    if weight <= limit:
        print("ready to fly")
    else:
        excess = weight - limit
        print(f"You need to remove {excess} kg. ")
        
weight = eval(input("Enter the weight:  "))
limit = eval(input("Enter limit allowed: "))
calculate_weight = check_suitcase(weight, limit)

