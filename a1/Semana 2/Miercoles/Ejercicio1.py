n = int(input("Introduce a number to know if it is prime or not: "))
cont = n-1
if n>=2:
    while n % cont != 0: 
        cont = cont - 1
        if cont == 1:
            break
    if n % cont == 0 and cont != 1 :
        print(f"The number {n} is not prime.")
    else :
        print(f"The number {n} is prime.")
else :
    print(f"The numebr {n} is not prime.")
