friends = ["Apple","Orange",5, 345.06, False, "Aakash", "Rohan"] # ye hai ak list of strings 

print(friends[0]) # ye hoti hai list or ap list ma se koi string change bhi krsakte ho 
friends[0] = "Grapes" # kuch is tarhaan
print(friends[0]) # to upr apple araha the print krne pr ab change hoke grapes araha 
#########
# unlike strings lists are mutable 
# strings are unmutable

# LIST INDEXING
# a list can be indexed just like a string 

# jese (apple 0) (orange 1) (5 2) (345.06 3) (False 4) (aakash 5) (Rohan 6) 
# or agar ap print(friends[0]) es 0 ki jgha agar koi or number jese 4 likhoo gy to False ayee ga aysy hi 6 pr Rohan 
print(friends[1:4]) # ap ye use kr ky list ko slice bhi krsakte hoo just like an string