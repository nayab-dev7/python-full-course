# break is used to come out of the loop when encountered
# it instructs the program to exit the loop now
#####################
# THIS IS HOW WE USE BREAK LOOPS

for i in range(100):
    if(i == 34):
        break # exit the loop right there at 34
    print(i)


# continue is used to stop the current iteration of the loop and continue
# with the next one it instructs the program to skip this iteration
#############################
# THIS IS HOW WE USE CONTINUE LOOPS

for i in range(100):
    if (i == 34):
        continue # skip this iteration iterate or iteration means i = 0 or i = 1 is iteration
    print(i)     # to ab ye 34 ko skip kare ga