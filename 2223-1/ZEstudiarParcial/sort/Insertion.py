def main():
    lista=[6 ,5 ,3,1,8,7,2,4]
    for i in range(len(lista)-1):
        max_indice=i
        if lista[max_indice]>lista[max_indice+1]:
            while True:
                aux=lista[max_indice]
                lista[max_indice]=lista[max_indice+1]
                lista[max_indice+1]=aux
                if max_indice!=0:
                    max_indice-=1
                if lista[max_indice]<=lista[max_indice+1]:
                    break
    
        
    print(lista)

main()
