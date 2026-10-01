d = {} # ye ak empty dict hai 
marks ={
    "harry": 100,
    "rizwaan": 56,
    "rohan": 23
}

print(marks.items()) # dict items method
print(marks.keys())  # marks ki keys dict keys method
print(marks.values()) # marks ki values show krne ke liye dict values method
marks.update({"harry": 99}) # ap ye dict update method use kr ky index ma koi new marks ya purani marks ko change krsakte ho
print(marks)

print(marks.get("harry2")) # prints none ## or ye get marks ko dhoonde ke liyee use hota hai
print(marks["harry2"]) # returns an erorr