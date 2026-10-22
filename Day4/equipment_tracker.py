def get_equipments():
    name = input("Enter equipment name:  ")
    daily_rental_rate = int(input("Enter rental daily rate: "))
    number_of_available_unit = int(input("Enter rental daily rate: "))
    
    #store data in dictionary
    equipment={
        "name" :name,
        "rate" : daily_rental_rate,
        "unit" : number_of_available_unit
        }
    
    
#collecting dictionary of product and storing into list
def collect_equipments():
    equipment_list = []
    answer = 'yes'
    while True:
        equipment = get_equipments
        equipment_list.append(equipment)
        if answer.lower().strip() == 'no':
            break
        else:
            print("Invalid entry. Only enter yes or no")
        answer=input("Add another equipment? yes/no:")
    return equipment_list


        

    
    
            
            