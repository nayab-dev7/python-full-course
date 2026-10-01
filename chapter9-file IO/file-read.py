# the random access memory is volatile , and all its contents are lost once program
# terminates in order to persist the data forever, we use files 

# A file is data stored in a storage device. A python program can talk to the file
# by reading content from it and writing content to it.


f = open("file.txt") # file path yaha daalna hai apne
data = f.read()  # ye file ke andr kia data hai osko read krta hai 
print(data) # ye jo file ke andr data mila hai osko print krta hai
f.close  # ye sara data read krne ke baad file ko close krta hai 