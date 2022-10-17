print("===========================================================\nThis program will tell tou wether a numer is perfect or not\n===========================================================")
n = int(input("Introduce a number: "))
dividers = []
aux = n-1
if n > 1:
    while aux >=1:
        if n % aux == 0:
            dividers.append(aux)
        aux = aux-1
    cont = 0
    for number in dividers:
        cont = cont + number
    if cont == n:
        print(f"The number {n} is a perfect number.")
    else :
        print(f"The number {n} is a not perfect number.")
