name = input("What is your name? \n \n").lower()    
gender = input("What is your gender? \n \n").lower()
if gender == "f" and name < "n" :
    print("Grupo A. ")
elif gender == "m" and name > "m" :
    print("Grupo A")
else : 
    print("Grupo B")