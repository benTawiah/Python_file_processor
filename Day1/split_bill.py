def split_bill(total_amount, people):
    if people <= 0:
        print("Number of people must be greater than zero.")
        return None
    else:
        each_person_pays = total_amount / people
        return each_person_pays
    


total_bill = float(input("Enter the total bill : "))
total_number_of_people = int(input("How many people are sharing the bill? "))
amount_per_person = split_bill(total_bill, total_number_of_people)

print(f"Each person should pay's: {amount_per_person} $")
    