# create a class with class a attribute a; = o. dose this change the attribute?
##############################

class demo:
    a = 4

o = demo()
print(o.a) # prints the class attribute bc instance attribute is not present
o.a = 0 # instance attribute is set
print(o.a) # prints the instance attribute bc instance attribute is present
print(demo.a) # prints the class attribute

# and ans is no it dose not change the attribute
