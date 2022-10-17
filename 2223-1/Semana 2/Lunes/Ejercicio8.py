income = float(input("How much money do you make in a year? \n "))
if income < 10000 :
    tax=income*0.05
elif income>=10000 and income <= 20000 :
    tax= income*0.15
elif income>20000 and income <= 35000 :
    tax = income * 0.2
elif income>35000 and income <= 60000 :
    tax= income * 0.3
elif income>60000 :
    tax = income * 0.45
print(f"\nYou owe {tax} to the state. ")