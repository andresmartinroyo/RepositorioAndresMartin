[6 ,5 ,3,1,8,7,2,4]

def selection(lista):
    for i in range(len(lista)):
        menor_valor=i
        for j in range(i+1,len(lista)):
            if lista[j]<lista[menor_valor]:
                menor_valor=j
        aux=lista[menor_valor]
        lista[menor_valor]=lista[i]
        lista[i]=aux
    
    print(lista)

selection([6 ,5 ,3,1,8,7,2,4])