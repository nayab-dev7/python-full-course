# create a class programmer for storing infoformation of few programmers
# woking at mircosoft.
#############################

class programmer:
    company = "mircosoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.pin = pin
        self.salary = salary

p = programmer("harry", 12000, 2499)
print(p.name, p.salary, p.company, p.pin)
r = programmer("rohan", 12000, 2499)
print(r.name, r.salary, r.company, r.pin)
