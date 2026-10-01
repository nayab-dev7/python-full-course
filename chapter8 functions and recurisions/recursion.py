# recursion is a function which calls itself.
# it is used to directly use a mathematical formula as function
##################
# factorial(n) = n x fractorial (n-1)
#####################################

'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 x 1
factorial(3) = 3 x 2 x 1
factorial(4) = 4 x 3 x 2 x 1 
factorial(5) = 5 x 4 x 3 x 2 x 1
factorial(n) = n x n-1 x........3 x 2 x 1
'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number: "))

print(f" the factorial of this number is: {factorial(n)} ")

# NOTE # programmer ko yaha buht dehan se kaam krna hai qk yaha ak loop chalta hai joke
       # chalta hi rehta hai band nai hota to osko band krne ke liyee sahi c