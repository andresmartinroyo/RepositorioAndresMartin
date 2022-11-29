
def insertion(lista):
    for i in range(len(lista)-1):
        maximo_valor=i
        while True:
            if lista[maximo_valor]>lista[maximo_valor+1]:
                aux=lista[maximo_valor]
                lista[maximo_valor]=lista[maximo_valor+1]
                lista[maximo_valor+1]=aux
                if maximo_valor!=0:
                    maximo_valor-=1
            else:
                break
        
    print(lista)
insertion([6 ,5 ,3,1,8,7,2,4])