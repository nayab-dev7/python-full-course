# write a program to find out whether a given post is talking about "harry" or not.
###########################

post = input("Enter the post: ")

if("harry" in post.lower()):
    print("this post is talking about harry")

else:
    print("this post is not talking about harry")