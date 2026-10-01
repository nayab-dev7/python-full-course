# can you change the self-parameter inside a class to somthing else
# say "harry" try changing self to "slf" or "harry" and see the effects.
#######################

from random import randint

class train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

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

# so the ans is han krsakte hain or program bhi intact rehy ga 