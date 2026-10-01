# instance attributes take preference over class attributes during assigment and
# retrivel
# when looking up for harry attribute it checks for the following 
#1 is attributes present in object?
#2 is attributes present in class?


class empolyee:
    language = "python" #class attribute
    salary = 120000

harry = empolyee()
harry.language = "javascript" # object attribute
print(harry.language, harry.salary)