def exponencial(n,exponente):
    if exponente == 0 :
        return 1
    return n*exponencial(n,exponente-1)

print(exponencial(int(input("Introduce la base: ")),int(input("Introduce el exponente: "))))