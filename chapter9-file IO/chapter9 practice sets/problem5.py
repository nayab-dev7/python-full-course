# repeat program 4 for a list of such words to be censored
###############################

words = ["donkey", "bad", "ganda"]

with open("donkey.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("donkey.txt", "w") as f:
    f.write(content)

# ab yaha pr humne pehlly words diye hain jo hide krne hain content se phir 
# file open ki data read kiya or in words ko replace kia phir 
# new data ko write kia ossi file ma 