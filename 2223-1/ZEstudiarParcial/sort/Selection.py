def main():
    lista=[6 ,5 ,3,1,8,7,2,4]
    for i in range(len(lista)):
        min_indice=i
        for j in range(i+1,len(lista)):
            if lista[j]<lista[min_indice]:
                min_indice=j
        aux=lista[min_indice]
        lista[min_indice]=lista[i]
        lista[i]=aux
    print(lista)

main()
