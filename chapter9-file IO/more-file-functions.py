# so agar files ma ak se ziayda lines hoo to osko read kese krte hain osko samjhte hain
# hum f.readlines function ka use kare gy python ma lines ko read krne ke liye 
# or wo humne list dedega ga lines ki ke kitni line hain or konsi type ki hain 
########################################

f=open("file.txt") # file open ki 

lines = f.readlines() # lines ko read kiya

print(lines, type(lines)) # lines ko print kia type ke sath

f.close

# ab ye to hogaya lines function ab dekhte hain line function 
# ab line function ak ak line ko indivisual read krta hai or data ko read krta hai 
# ak ak line se data read krna chalo dekte hain kese hota hai 
 #############################################

f=open("file.txt") #file open ki 

line1 = f.readline() # line1 ko read kia phir line1 fo print kia type ke sath
print(line1, type(line1))

line2 = f.readline() # line1 ko read kia phir line1 fo print kia type ke sath
print(line2, type(line2))

line3 = f.readline() # line1 ko read kia phir line1 fo print kia type ke sath
print(line3, type(line3))

line4 = f.readline() # ab humari file ma 4th line nai hai to yaha empty string ayee ga output ma
print(line4 == "")

f.close # file close krdi 


# ab ye to hogaya ke lines or line kese read krte hain 
# ab dekhte hain ke isko whileloop ma kese krte hain 
# whileloop lines print krta rahe ga jab tak sari khatam na hojayee 
##########################################

f=open("file.txt") # file open ki 

line = f.readline() # lines read ki 
while(line != ""): # ab while line is not equal to an empty string 
    print(line) # to tab tak lines print karte jaooo jab tak empty line na ayee
    line = f.readline() # ab osko sari lines ko read kro or print 

f.close # file close