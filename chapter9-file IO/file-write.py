# this is how you can make files and write whitin them using write function in python
#  ab ye ak new file banaee ga isi folder ma myfile.txt naam se or osme ye string wali data ko write kare ga 
##############################################################



st = "harry is a good boy"  # humne ak string li osme data likhaa jo write krna hai file hai 

f = open("myfile.txt","w") # yaha humne open function or "w" write ka use kr ke file banaii 

f.write(st)   # yaha os string jo humne banaii thi osko write kiya 

f.close     # or yaha humne f.close ka use krke file ko close krdia 