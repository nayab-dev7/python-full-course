# ab dekhte hain append mod kia krta hai 
# ye file ke last ma kuch bhi add krne ke liyee use hota hai
# jitni baar ap isko chalaoo gy ye file ke end ma add krta jayee ga jo ap isko bolo gy 
########################################################



st = "harry is a good boy"  # ab humne ye string add krni hai apni file ma append mod ka use kr ky 

f = open("myfile.txt","a")   # yaha humne file kholi or append mod ka use kiya 

f.write(st)   # yaha wo append mod ki gaii string add hui file ke end ma write hui 

f.close     # file close 