# write a program to find out whether a file is identical and matches the content
# of another file.
##############################

with open("this.txt") as f:
    content1 = f.read()

with open("this_copy.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("yes these files are identical")

else:
    print("no these files are not identical")


# ab yaha pr humne function ka use kr ky file 1 or file 2 ko khola 
# phir if/else loop ka use kr ky 2 conditions bana di agar content 1 = hai content 2 ke to 
# if call hoga agar content 1 = nai hai content 2 ke to else funtion call hoga 