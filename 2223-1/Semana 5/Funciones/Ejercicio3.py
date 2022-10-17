def factorial(n):
    aux=n
    fact=1
    while aux>1:
        fact*=aux
        aux-=1
    return fact

print(factorial(int(input("Introduce un numero: "))))
