# write a program to print multipilication table of n using 
# loops in reversed order.
##########################

n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} X {11 -i} = {n*(11-i)}")