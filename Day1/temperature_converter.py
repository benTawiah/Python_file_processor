def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

temp_in_fahrenheit= eval(input("Enter a temperature in Fahrenheit: ")) #eval automatically convert the data type to what is requires, without specifying the data type by hand
temp_celcius = fahrenheit_to_celsius(temp_in_fahrenheit)
print(temp_in_fahrenheit, "fahrenheit", temp_celcius, "degree celcius" )
