
def get_meal():
    meal_list = []
    answer = 'yes'
    while True:
        if answer == "yes".lower():
            meal_name = input("Enter meal name: ")
            time = float(input("Enter preparation time: "))
            vegi = input("Are you vegetarian: ")
            meal = {
                "meal name": meal_name,
                "time": time,
                "vegi": vegi
            }
            meal_list.append(meal)

        elif answer == "no".lower():
            break

        answer = input("Add another product? yes/no: ").lower()

        if answer not in ["yes", "no"]:
            print("Invalid response. Enter yes/no")

    return meal_list


def find_quick_meals(meals, available_minutes):
    meal_list = []
    for meal in meals:
        if meal['time'] <= available_minutes:
            meal_list.append(meal)
            
        else:
            print("No meals fit your available time")
    for chosen in meal_list:
        print ("This is what is available to you", chosen)
        


def show_meals(meal):
    for key, value in meal.items():
        if key == "time":
            print(f"{key.capitalize()} : {value:.2f} minutes")
        elif key == "meal name":
            print(f"{key.capitalize()} : {value}")
        else:
            print(f"{key.capitalize()} : {value}")


time_available = int(input("How much time do you have: "))

meals = get_meal()

for meal in meals:
    print("\n--- meals ---")
    show_meals(meal)


meal_menu = meals
new_meal = find_quick_meals(g, time_available)
print(new_meal)
