def get_repair():
    #get data from user
    name = input("Enter equipment name: ")
    location = input("Enter location: ")
    priority = input("Choose priority: high or normal ")
    status = input("Resulution status yes or no ")
        
    #store data in dictionary
    equipment ={
       "name": name,
       "location": location,
       "priority": priority,
       "status": status 
    }
        
    #collecting dictionary of product and storing into list
def collect_equipments():
    my_equipment =[]
    answer == 'yes'
    while True:
        if answer == 'yes':
            repair = get_repair()
            my_equipment.append(repair)
            answer = input("Do you have additional equipment to add, yes or no")
        elif answer.lower().strip() == 'no'():
            break
        else:
            print ("Accepts only yes and no.")  
        answer =  input("Add another product? yes/no:")
        return my_equipment

def find_urgent_repairs(repairs):
    priority_list = []
    for repair in repairs:
        if repair['priority'] == "high".lower():
            priority_list.append(repair)
    return priority_list
    
def show_repair(repair):
    for key, value in repair.items():
        if key == 'name':
            print(f"Equipment: {value.capitalize()}")
        elif key == 'location':
            print(f"Location: {value.capitalize()}")
        elif key == 'priority':
            print(f"Priority: {value.capitalize()}")
        else:
            print(f"Resolved: {value.capitalize()}")
        
            
        
            
            

equip = collect_equipments()
print(equip)
urgent = find_urgent_repairs(equip)

for euipment in urgent:
    print("\n--- Urgent repairs: ---")
    show_result = show_repair(euipment)


