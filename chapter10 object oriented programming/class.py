class employee:
    language = "py" # this is a class attribute
    salary = 12000


harry = employee() 
harry.name = "harry" # this is a instance atrribute
print(harry.name, harry.language, harry.salary)

rohan = employee()
rohan.name = "rohan"
print(rohan.name, rohan.language, rohan.salary)

# here name is instance attrinute and salary and language are class attributes
# as they directly belong to the class 