print("============================================================\nThis program exists for you to know if you have to pay taxes\n============================================================\n")
age = int(input("How old are you?\n"))
income = float (input("How much money do you make monthly? \n "))
if income >= 1000 and age >= 16 :
    print("You have to pay taxes")
else :
    print("You are save from the IRS from now")
    