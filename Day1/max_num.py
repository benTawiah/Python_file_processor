def max_number(number):
    max=0
    for i in my_list:
        if i > max:
            max=i
    return max
            
my_list=[78,99,32,100,89]
max_number = max_number(my_list)
print("The maximum number in the list is ", max_number)