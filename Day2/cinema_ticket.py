movie={
    "title": "Movie Title",
    "ticket_price": 9.50,
    "available_seats": 30
}

seat_available=int(input("How many additional ticket : "))
updated_available_seat=movie['available_seats'] + seat_available

request=int(input("How many ticket do you want to buy?  "))

if request > 1 and request >= updated_available_seat :
   ticket_number= request - updated_available_seat
   total_ticket_cost= request * movie["ticket_price"]
   print("The cost for requested ticket is ", total_ticket_cost)
