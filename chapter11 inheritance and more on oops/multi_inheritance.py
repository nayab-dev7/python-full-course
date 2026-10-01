class employee:
    company = "ITC"
    name = "default name"
    def show(self):
        print(f"the name of the employee is {self.name} and the company is {self.company}")

class coder:
    language = "python"
    def printlanguages(self):
        print(f"out of all the languages here is your language: {self.language}")



class programmer(employee, coder):
    company = "ITC infortech"
    def showlanguages(self):
        print(f"the name is {self.company} and he is good with {self.language} language")


a = employee()
b = programmer()

b.show()
b.printlanguages()
b.showlanguages()

