def main():
    tupla=(
        [313, 6786, 5151], [1, 4, 10], [41, 53, 86, 56, 12],
        [84, 4], [], [35, 4, 1, 2],
        [1, 4], [5], [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [100, 84, 4781], [], [53, 56, 1, 4, 45],
        [84, 88, 407], [153, 25], [10, 35, 9474],
            )
    for lista in tupla:
        for numero in lista:
            num=numero*6
            divisores=[]
            for i in range(1,numero):
                if num%i==0:
                    divisores.append(i)
            for index in range(len(divisores)):
                if (divisores[index]+1) in divisores and (divisores[index]+2) in divisores:
                    print(f"El número {num} es triangular piramidal.")
                    break
main()