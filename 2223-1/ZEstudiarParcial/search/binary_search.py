def quicksort(lista):
    if len(lista)<=1:
        return lista
    else:
        pivote=lista.pop()
        mayores=[]
        menores=[]
        for n in lista:
            if n < pivote:
                menores.append(n)
            else: 
                mayores.append(n)
        return quicksort(menores) + [pivote] + quicksort(mayores)
        
def binarysearh(lista_ordenada,numero):
    i=0
    j=len(lista_ordenada)
    objetivo=numero
    promedio=(i+j)//2
    if lista_ordenada[promedio]>objetivo:
        if len(lista_ordenada)==1:
            return False
        return binarysearh(lista_ordenada[i:promedio],objetivo)
    elif lista_ordenada[promedio]<objetivo:
        if len(lista_ordenada)==1:
            return False
        return binarysearh(lista_ordenada[promedio:j],objetivo)
    elif lista_ordenada[promedio]==objetivo:
        return True

if binarysearh(quicksort([6 ,5 ,3,1,8,7,2,4]),8):
    print("El numero esta.")
else:
        print("El numero no esta.")