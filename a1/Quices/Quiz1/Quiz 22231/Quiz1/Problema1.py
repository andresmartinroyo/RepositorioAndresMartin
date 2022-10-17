tupla = ([313, 153, 370], [], [31, 515, 78593, 3819, 12],
[407, 9041], [371, 706], [407,153, 1, 2],
[41, 4], [5], [1, 2, 3, 4, 5, 6, 7, 8, 9],
[313, 54748, 370], [], [31, 515, 432, 313, 45],
[313, 88, 407], [153, 370], [1634, 8208, 9474],)


for lista in range(len(tupla)):
    for numeros in range(len(tupla[lista])):
        suma=0
        n=tupla[lista][numeros]
        n=str(n)
        for digitos in range(len(n)):
            suma+=int(n[digitos])**3
        if suma==int(n):
            print(f"El número {n} es narcisista.")