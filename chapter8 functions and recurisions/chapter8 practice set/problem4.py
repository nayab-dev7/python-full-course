# write recursive function to calculate the sum of first N numbers.
#################################
# ye sum aysy work krta hai samjhna muskil hai or zarori bhi ye ak loop ma chalta hai
#  jab tak values complete na hojayee tab tak loop chalta rehta hai

'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1+2+3+4..........n -1+n
sum(n) = sum(n-1) + n
'''
def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

print(sum(4))
