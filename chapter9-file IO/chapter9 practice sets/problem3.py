# write a program to generate multiplication tables from 2 to 20 and write it to 
# different files place these files in a folder for a 13 year old.
############################################

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)


for i in range(2, 21):
    generateTable(i)

# ab yaha pr humne def function ka use kiya hai program banna ne ke liye or for i in range ka use kiya hai table print krne ke liye 
# or phir with open ka use kr ke ak folder banays hai or phir har table ki file alag alag banaii hai 
# or un files ma tables ka data write kiya hai 