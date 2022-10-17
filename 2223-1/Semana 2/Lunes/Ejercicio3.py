print( "This program will tell you if a number you write is even or odd.")
n= input("Insert your number: ")
n_numeric= True
if n.isnumeric():
    n = int(n)
else :
    n_numeric = False
if n_numeric == True:
    if n%2 == 0:
        print(f"The number{n} is even")
    else :
        print("The number {} is odd".format(n))     