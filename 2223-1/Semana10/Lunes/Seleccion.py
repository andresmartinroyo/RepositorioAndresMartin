def main():

    lista=[6 ,5 ,3,1,8,7,2,4]
    indice=0
    for i in range(len(lista)):
    
        menor =i
        for j in range(i+1,len(lista)):
            if lista[j]<lista[i]:
                menor = j
        aux=lista[i]
        lista[i]=lista[menor]
        lista[menor]=aux

    print(lista)

main()


            