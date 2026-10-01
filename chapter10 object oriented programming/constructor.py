# __init__() constructor
# __init__() is a special method which is first run as soon as the object is created
# __init__() method is also known as constructor 
# it takes self-arguments and can also take arguments.
# donder methods
########################################


class employee:
    language = "python"
    salary = 120000

    def __init__(self, name, salary, language):
        self.name=name 
        self.salary=salary
        self.language=language
        print("i am creating an abject")

    def getInfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")

    def greet():
        print("good morning")


harry = employee("harry", 130000, "javascript")
print(harry.name, harry.salary, harry.language)