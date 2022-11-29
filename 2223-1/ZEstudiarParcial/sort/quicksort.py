def quicksort(lista):
    if len(lista)<=1:
        return(lista)
    else:
        pivote=lista.pop()
    
    mayores=[]
    menores=[]
    for n in lista:
        if pivote>n:
            menores.append(n)
        else:
            mayores.append(n)
    return quicksort(menores)+[pivote]+quicksort(mayores)

print(quicksort([6 ,5 ,3,1,8,7,2,4]))

