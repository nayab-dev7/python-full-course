# write a program to make a copy of text file "this.txt"
############################

with open("this.txt") as f:
    content = f.read()

with open("this_copy.txt", "w") as f:
    f.write(content)



# yaha bhi wahi kia file open phir content read 
# oske baad phir file open pr is bar write mode ma "W" 
# phir new file banaii previous file ki copy 