import random  # moduel import krta hai 
'''
1 for snake 
-1 for water
0 for gun
'''
computer = random.choice([-1, 0, 1])  # computer har bar random numbers pick kare ga 
youstr = input("Enter your choice: ")  # yaha pr tum kia choose karo ge wo input hai 
youDict = {"s": 1, "w": -1, "g": 0}  # tum bhi 3 chizze choose krsakte hoo
reverseDict = {1: "snake", -1: "water", 0: "gun"}  # wo 3 chizze ye hain

you = youDict[youstr] # by now we have 2 numbers (veriables), you and computer 


print(f"You chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")   # ye reverse dictionary ka use kr ky pata kare ga ke tumne kiya choose kiya hai

if(computer == you): # yaha se sara if or else ka loop start hota hai 
    print("its a draw")

else:
    if(computer ==-1 and you ==1):
        print("You Win!")

    elif(computer ==-1 and you ==0):
        print("You Lose!")
    elif(computer ==1 and you ==-1):
        print("You Lose!")

    elif(computer ==1 and you ==0):
        print("You Win!")

    elif(computer ==0 and you ==-1):
        print("You Lose!")

    elif(computer ==0 and you ==1):
        print("You Win!")

    else:
        print("somthing went wrong!")

