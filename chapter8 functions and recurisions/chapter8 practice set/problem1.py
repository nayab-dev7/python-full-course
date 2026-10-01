# write a program using function to find greatest of three numbers.
########################

def greatest(a, b, c): # yaha se function start hota hai 
    if(a>b and a>c): # yaha pr hum bata rahe hain ke function ko kia krna hai or yahi se if/else loop start horaha hai
        return a
    
    elif (b>a and b>c):
         return b

    elif(a, b, c):
        if(c>a and c>b):
         return c  # yaha pr loop break hota hai or function close hota hai 
    
a = 1 # yaha pr hum numbers add krsakte hain or jo bhi sabse bara number hoga wo print hoga
b = 23
c = 55

print(greatest(a, b, c)) # ye raha print krne ka command 
