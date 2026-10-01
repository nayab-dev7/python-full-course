# write a pyton function to print multiplication table of a given number,
##########################

def multiply(n): # yaha se sara function start hota hai def function ko call krne ke liyee use kia jata hai
    for i in range(1, 11): # ye range btaii hai humne is function ko ke 1, se 11, tak krta hai multiply to ye 1, se 10 tak kare ga qk python ga 0 se start hote hain numbers
        print(f"{n} X {i} = {n*i}")  # ye n to multiply kare ga i se 

multiply(5)  # yaha ap jo numbers add kro gy unka table ban jaye ga ap int input ka use karke user se input bhi karwaa sakte hoo numbers