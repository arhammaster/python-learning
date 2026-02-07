# Write Python program : 
#
# [x] Define Airplane class allow to create Airplane with number of seats
# [x] it should allow user to book ticket with name
# [x] it should show how many seats are available so that user can book his / her tickets to travel
# [x] in should allow user to cancel ticket 
# [-] if all seats (tickets) are booked it should not allow to book more ticket and print Airplane already book 

# Test data
#
# create Airplane CA(3) SA(2) BA(2)
# demonstrate CA booking with all passenger and show "No available seats" when 4th person try to book
# [-] demonstrate SA Airplane booking and cancel 
# demonstrate BA booking and allow 1 seats is available 

class Airplane :

    def __init__ (self,seats:int,flight_name:str,seats_booked) :
        self.seats:int = seats
        self.flight_name:str = flight_name
        self.seats_booked:int = seats_booked

    def seats_available (self) :
        print(f"{self.flight_name}, seats available are {self.seats  - self.seats_booked}")

    def booking (self,user_name:str) :
        if self.seats_booked != self.seats :
            self.seats_booked += 1
            print(f"{self.flight_name} flight booked for {user_name} ")
        else :
            print(f"All seats are booked sorry {user_name}")

    def canceling (self,user_name:str) :
        self.seats_booked -= 1
        print(f"{self.flight_name} flight canceled for {user_name} ")


ca = Airplane (3,"Ca",0) 
sa = Airplane (2,"SA",0)
ba = Airplane (2,"Ba",0)

ca.booking("Jack")
ca.booking("Jill")
ca.booking("Mario")
ca.booking("Tom")
ca.canceling("Mario")
ca.booking("Tom")

sa.booking("Tom")
sa.canceling("Tom")

ba.booking("Tom")
ba.seats_available()


