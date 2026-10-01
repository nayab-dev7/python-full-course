# write a program to find out the line number where python is present from ques 6
########################################################

with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"yes python is present. line no: {lineno}")
        break
    lineno += 1

else:
    print("no python is not present")


# to yaha pr humne wahi sab kiya pehly file open ki phir f.readline ka use karke total lines check ki
# phir if/else ka loop laga kr program ko btaya ke print kare agar python hai to konsi line ma hai 
# or agar if condition setisfy hogaii to else conditon skip hogi nai to else conditon chale gi 
