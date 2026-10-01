# a function can be accept some value it can work with 
# we can put these values in the parentheses.


#########################

def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)

goodDay("harry", "Thankyou")
# to ye kuch aysy kaam kr raha hai ke humne name or ending ki 2 fixed values dydi
# or def function ka use kr ky humne python ko btaya ke kia krna hai 

# a function can also return value as shown below.

def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "ok"  

a = goodDay("Harry", "Thank You")
print(a) 

# ab ye return "ok" ne function ko khatam krdia or agy continue hua index
# ya phir ye samjh lo ke def ke pass value thi osne wo value ak veriable ko di
# phir return hoke wait krne laga ke phir agar yahi value kisi or veriable ko chaiyee to ye dega
