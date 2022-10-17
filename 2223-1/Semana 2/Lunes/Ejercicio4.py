print("============================\nWelcome to this pizza place!\n============================")
PizzaType=input("What type of pizza will you have?\n1.-Vegetarian.\n2.-Carnivore.\n==>")
if PizzaType == "1" :
    PizzaType="vegetarian"
elif PizzaType == "2" :
    PizzaType="carnivore" 
else :
    print("Error")
if PizzaType=="vegetarian":
    topping = input("What topping will you like with your pizza:\n1.- Tofu.\n2.-Pepper.\n==>")
    if topping == "1":
        topping="tofu"
    elif topping == "2":
        topping= "pepper"
    else : 
        print("error")
elif PizzaType=="carnivore":
    topping = input("What topping will you like with your pizza:\n1.- Ham.\n2.-Pepperoni.\n==>")
    if topping == "1":
        topping="ham"
    elif topping == "2":
        topping= "pepperoni"
    else : 
        print("error")
print(f"Youll be having {PizzaType} with {topping}.")