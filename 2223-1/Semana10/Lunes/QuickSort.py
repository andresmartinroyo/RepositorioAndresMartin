def quicksort(lista):
    if len(lista)==1:
        return lista
    menor, pivote, mayor=particion(lista)
    lista2 = quicksort(lista)
    print(lista2)

def particion(lista):
    menor=[]
    mayor=[]
    pivote=lista[0]
    for i in range(len(lista)):
        if lista[i]<pivote:
            menor.append(lista[i])
        elif lista[i]>pivote:
            mayor.append(lista[i])
    return quicksort(menor)+ [pivote]+ quicksort(mayor)

def main():
    lista=[6 ,5 ,3,1,8,7,2,4]
    quicksort(lista)

main()