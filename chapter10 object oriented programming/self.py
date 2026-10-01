# self refers to the instance of the class it is automatically passed with a function call from an abject
##########################################


class empolyee: # class atteibute
    language = "python"
    salary = 120000

    def getInfo(self): # function inside class
        print(f"the language is {self.language}. the salary is {self.salary}")
############################################
# static method 
# sometimes we need a function that dose not use the self-parameter
# we can define a static method like this:
    @staticmethod
    def greet(self): # static function
        print("good morning")

harry = empolyee() # object attribute
harry.language = "javascript"
harry.greet()
harry.getInfo()

