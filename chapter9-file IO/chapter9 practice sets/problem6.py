# write a program to mine a log file and find out whether it contains "python".
########################################

with open("log.txt") as f:
    content = f.read()

if("python" in content):
    print("yes python is present")
else:
    print("python dose not present")

# ab yaha pr humne file open ki phir data read kiya or phir 
#' if/else ka loog lagaya agar if ma data mil gaii to if chale ga 
# agar if ma data na mili to else chale ga 