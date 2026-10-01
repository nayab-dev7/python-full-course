# write a program to greet all the person names stored in a list 
# l and which starts with S
# you can pick any persons names as a list 
##########################


l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello: {name}")
