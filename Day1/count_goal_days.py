def count_goal_days(daily_steps,goal):
   
    count = 0 
    for step in daily_steps:
        if step >= goal:
            count += 1
    
        
goal_steps = int(input("Enter your daily step goal: "))    
number_days = 7
walks = 0
my_list=[]
while walks < number_days:
    steps = eval(input("Enter your daily steps: "))
    my_list.append(steps)
    walks += 1
successful_days= count_goal_days(my_list, goal_steps)


if successful_days == len(steps):
    print("Perfect week!")
elif successful_days >= 1:
    print("You have reached your goal", successful_days, "out of", len(steps))
    print("Good progress.")
else:
    print("A fresh start tomorrow!")
