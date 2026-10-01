# in while loops the condition is checked first. if it evaluates to true
# the body of the loop is executed otherwise not
##############################
# if the loop id entered the process of condition check and execution 
# is continued until the condition becomes false.
#########################

i = 1 

while(i<6):
    print(i)
    i = i + 1 # or i +=1
'''
output:
1
2
3
4
5
'''
##########
# NOTE: if the condition never become false the loop keeps getting executed
