import random 

class Train:
    def __init__(self):
        self.Train_name=""
        self.Train_number=0
        self.station_1=""
        self.station_2=""
        self.Total_seats=200
        self.Fare_per_passenger=0
        self.passenger_name=""
        self.passenger_age=0
        self.Seats_booked=0
        self.booking_status=False

    def input(self):
        self.Train_name=input("Enter the name of the train :")
        self.Train_number=int(input("Enter the number of the train :"))
        self.station_1=input("Enter the your pick up station :")
        self.station_2=input("Enter the your destination  :\n")

    def fare_calculation(self):
        fare ={"short":(700,800),"mid":(1000,1200),"long":(1200,1400)}
        journey=input("Enter the type of ride (short/mid/long):\n")
        while journey not in fare :
            print("Wrong output !!")
            journey=input("Enter the type of ride (short/mid/long):\n")
        minimum,maxmium = fare[journey]
        price= random.randint(minimum,maxmium)
        self.Fare_per_passenger=price
        

    def display_details(self):
        print(f"The name of the train :{self.Train_name}")
        print(f"The train number is : {self.Train_number}")
        print(f"Your pickup is in {self.station_1}")
        print(f"Your destination is {self.station_2}")
        print(f"The total available seats are : {self.Total_seats}\n")

    def passenger_booking(self):
        self.passenger_name=input("Enter the name : ")
        self.passenger_age=int(input("Enter the age :"))
        self.Seats_booked = int(input("Enter number of seats: \n"))
        if self.Seats_booked<=self.Total_seats:
            print("Booking succesfull!!")
            self.Total_seats -=self.Seats_booked
            self.booking_status=True
        else:
            print("Booking unsuccesfull ..limit reached \n")

    def total_fare_calculation(self):
        total=self.Fare_per_passenger*self.Seats_booked
        print(f"The total fare is :{total}")

    def booking_status_check(self):
        if self.booking_status:
            print("Ticket is booked successfully.")
            print(f"Passenger: {self.passenger_name}")
            print(f"Seats booked: {self.Seats_booked}\n")
        else:
            print("No booking found.")

    def cancel_ticket(self):
        if self.booking_status:
            self.Total_seats += self.Seats_booked
            self.Seats_booked = 0
            self.booking_status = False
            print("Ticket cancelled successfully.\n")
        else:
            print("No booking found.\n")


train = Train()
train.input()
train.fare_calculation()

while True:
    print("\n1. Display Train Details")
    print("2. Book Ticket")
    print("3. Calculate Total Fare")
    print("4. Check Booking Status")
    print("5. Cancel Ticket")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        train.display_details()

    elif choice == "2":
        train.passenger_booking()

    elif choice == "3":
        train.total_fare_calculation()

    elif choice == "4":
        train.booking_status_check()

    elif choice == "5":
        train.cancel_ticket()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")

    cont=input("Do you want to continue (yes/no):")
    if cont.lower()!='yes':
        break