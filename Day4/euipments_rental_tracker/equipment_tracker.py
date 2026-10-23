def get_equipments():
    name = input("Enter equipment name:  ")
    while True:
        try:
            daily_rental_rate = float(input("Enter rental daily rate: "))
            if daily_rental_rate < 0:
                print("Input should not be negative.")
            else:
                break     
        except ValueError:
            print("Invalid Rate. Please enter a number.")
    while True:    
        try:
            number_of_available_unit = int(input("Enter available unit: "))
            if number_of_available_unit < 0:
                print("Available quantities must be non-negative whole numbers. ")
            else:
                break
        except ValueError:
            print("Invalid Quantity. Please enter a number. ")
            
            
    #store data in dictionary
    equipment={
        "name" :name,
        "rate" : daily_rental_rate,
        "unit" : number_of_available_unit
        }
    return equipment
    
    
#collecting dictionary of product and storing into list
def collect_equipments():
    equipment_list = []
    answer = 'yes'
    while True:
        if answer.lower().strip() == 'yes':
            equipment = get_equipments()
            equipment_list.append(equipment)
        elif answer.lower().strip() == 'no':
            break
        else:
            print("Invalid entry. Only enter yes or no")
        answer=input("Add another equipment? yes/no:")
    return equipment_list

def show_equipment(equipment):
    for key, value in equipment.items():
        if key == "rate":
            print(f"{key.capitalize()} : €{value:.2f}")
        elif key == "unit":
            print(f"{key.capitalize()} : {value} units")
        else:
            print(f"{key.capitalize()} : {value.capitalize()} ")
            
import json
def save_content(rental):
    with open('rental.json', "w", encoding="utf-8") as file:
        json.dump(rental, file, indent=4, ensure_ascii=False)
        
def load_content():
    with open('rental.json', 'r', encoding="utf-8") as file:
        content=json.load(file)
    return content

        

    
    
            

coll_equip = collect_equipments()
save_content(coll_equip)

content_load = load_content()
content_load.extend(coll_equip)

for equipment in coll_equip:
    print("--------Equipment----------")
    show_equipment(equipment)          