import os 

diretorio = "temp"
if not os.path.exists(diretorio):
    os.mkdir(diretorio)
with open("temp/temp.txt", "w") as file: 
    pass
