class Train:
    def __init__(self, name, fare, seats) -> None:
        self.name=name
        self.fare=fare
        self.seats=seats

    def getFare(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in this train are {self.seats}")

    def fareInfo(self):
        print(f"the price of the ticket is Rs {self.fare}")

    def bookTicket(self):
        if self.seats>=0:
            print(f"your ticket has been booked! Your seat is {self.seats}")
            self.seats= self.seats -1
        else:
            print("Sorry this train is full kindly book in tatkal")

    def cancleTicket(self,seatNo):
        pass



intercity=Train("Intercity Express 21652", 90, 300)
intercity.getFare()
intercity.fareInfo()
intercity.bookTicket()
print("")
intercity.bookTicket()



