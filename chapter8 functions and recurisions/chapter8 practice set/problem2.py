# write a python program using function to convert celsius to fahrenheit.
#################

def f_to_c(f): # yaha se function start horaha hai 
    return 5*(f-32)/9 # yaha pr humne function ko btaya hai ke fahrenheit ko kisse devied krna hai


f = int(input("Enter temperature in F: ")) # yaha pr hum user se input ly rahe hain celsius ma 
c = f_to_c(f) # yaha pr celsius fahrenheit ma change horaha hai 
print(f"{round(c, 2)}°C") # ye print krne ka command hai