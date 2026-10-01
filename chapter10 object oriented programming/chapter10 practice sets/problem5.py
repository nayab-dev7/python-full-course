# write a class train which has methods to book a ticket get status 
# no fs seats and get fare information of the train running under indian railways.
##############################

from random import randint

class train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
        
    def getstatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getfare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")



t = train(12399)
t.book("rampur", "delhi")
t.getstatus()
t.getfare("rampur", "delhi")