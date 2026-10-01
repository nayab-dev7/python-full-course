# create an empty dictionary allow 4 friends to enter their fav languages as 
# value and use key as thier names assume that the names are unique 


d =  {}
name = input(" Enter friends name: ")
lang = input("Enter language naem: ")
d.update({name: lang})

name = input(" Enter friends name: ")
lang = input("Enter language naem: ")
d.update({name: lang})

name = input(" Enter friends name: ")
lang = input("Enter language naem: ")
d.update({name: lang})

name = input(" Enter friends name: ")
lang = input("Enter language naem: ")
d.update({name: lang})

print(d)
