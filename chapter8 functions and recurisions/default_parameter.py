# we can have value as default as default argument in a function.
# if we specify name = "stranger" in the containing def, 
# this value is used when no argument is passed.


def goodDay(name, ending="thank you"): # defualt ending
    print(f"Good Day, {name}")
    print(ending)

goodDay("Harry", "Thanks") # the ending ive told the function
goodDay("Rohan")


# to agar main isko btaoon ga ke ending kia deni hai to ye wahi ending dega 
# lekin agar na btaoon to ye default ending use kre ga joke hai "thank you"
# Agar string ke andar kuch dynamic daalna hai (jaise variable ya number),
# to shuru mein f lagao. Agar sirf simple text likhna hai jaise "good day",
# to f lagane ki zaroorat nahi hai.
# ye jo code ki 7th line pr print(f"Good....") iski bat kr raha main