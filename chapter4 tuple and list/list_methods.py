friends = ["Apple","Orange",5, 345.06, False, "Aakash", "Rohan"]
print(friends) 

friends.append("Harry") # main ne ye append use kiya "Harry" word ko list ma add krne ke liyee 
print(friends)



###############
# to ye sare methods hain jo ap use krsakte ho 
# example L1 = [1,8,7,2,21,15]
# L1.sort(): updates the list to [1,2,7,8,15,21]
# L1.reverse(): updates the list to [15,21,2,7,8,1]
# L1.append(8) adds 8 at the end of the list 
# L1.insert(3,8) this will add 8 at 3 index
# L1.pop(2) will delete element at index 2 and return its value 
# L1.remove(21) will remove 21 from the list 

l1 = [1,8,7,2,21,15] # sort method
l1.sort()
print(l1)

l1 = [1,2,3,4,6,5,3,8,] # reverse method
l1.reverse()
print(l1)

l1 = [1,2,5,4,7,9,0,] # insert method
l1.insert(3,3333)
print(l1)

l1 = [1,4,32,6,8,9,] # pop method
l1.pop(1)
print(l1)

l1 = [2,4,6,8,2,1,9] # remove method
l1.remove(4)
print(l1)


###########################
# PYTHON SHORTCUT
# agar apko terminal ma koi file run krni hai to ap krsakte ho
# python .\filename.py ye use kr ky pr apka pythonn apke folder ma on hoo 
# ye tabhi work kare ga phir 