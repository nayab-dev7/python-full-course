# sometimes we want to play pubg on our phone if the day is sunday 
# sometimes we order ice cream online if the day is sunny 
# all these are decisions which depend on a condition being met
# in python programming too we must be able to execute instructions on a conditions being met
##############################

# IF ELSE AND ELIF IN PYTHON

a = int(input("Enter your age: "))

if(a>=18):
    print("you are above the age of consent")
    print("good for you")

elif(a<0):
    print("aby chutiya hai kia?")

elif(a==0):
    print("aby gandu insaan")

else:
    print("you are below the age of consent")

###########
# agar if ki condition true hogi to else nai chale ga 
# or agar if ki condition false hogi to else chale ga
# or agar apne if else elif likhaa to ye teeno apas ma connected hain
