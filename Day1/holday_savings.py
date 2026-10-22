def holiday_savings(target, monthly_saving):
    if target <= 0 or monthly_saving <= 0:
        print("Please enter positive amounts.")
        
        
    else:
        total_savings = 0
        months = 0
        while total_savings < target:
            total_savings += monthly_saving
            months += 1
        print(f"It will take {months} months to save ${target}.")

holiday_target = float(input("Enter your holiday savings target: "))
monthly_saving_amount = float(input("Enter your monthly saving amount: "))
        
holiday_savings(holiday_target, monthly_saving_amount)

