age = int(input("How old are you? \n\n"))
cost = 0
if age<4:
    cost =cost
elif age >= 4 and age < 18 :
    cost = 5
else :
    cost =10
print(f"\nYou have to pay {cost} $, because you are {age} years old.")