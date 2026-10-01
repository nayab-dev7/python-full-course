'''write a program to read the text from a given file poems.txt and find out
whether it contains the word "twinkel"'''
####################################

f=open("poem.txt") # file open ki poem.txt wali 
content=f.read() # file ka content read kiya 
if("twinkel" in content):    # ab yaha if/else loop lagya if ma twinkel in content agar hai to 
    print("the word twinkel is present in the content:  ")  # print hoga ye wrna 

else:
    print("the word twinkel is not present in the content: ") # print hoga ye agar if condition mil jati hai to else nai chale ga 
    
f.close
