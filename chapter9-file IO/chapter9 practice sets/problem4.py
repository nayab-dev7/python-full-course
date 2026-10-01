# a file contains a word donkey multiple times you need to write a program
# which replace this word with #### by updating the same file.
######################

word = "donkey"

with open("donkey.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "#####")

with open("donkey.txt", "w") as f:
    f.write(contentNew)


# ab yaha pehly humne donkey word add kiya hai phir wo file open ki hai phir data read kiya hai 
# phir data replace kia hai or phir ossi file ma new data ko write kia hai 