f = open("file.txt") # file ko open kiya 
print(f.read())   # print kiya jo data read hua oske baad 
f.close  # flie close ki 

# the same can be written by using with statment like this:
with open("file.txt") as f: # yaha open with ka use kiya or file ko read kiya as f 
    print(f.read())  # or yaha bs wahi data jo read kia tha wahi print kiya 

# you dont have to explicitly close the file 
# apko file close krne ki zarorat nai ab ye open with wala program khud hi file close krde ga data read krne ke baad 