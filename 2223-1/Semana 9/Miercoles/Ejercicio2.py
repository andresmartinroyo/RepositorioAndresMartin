

def leer_lista(lista,elemento_a_buscar):
    if lista==None:
        return f"El elemento {elemento_a_buscar} no esta"
    if lista is list:
        if lista[len(lista)-1]!=elemento_a_buscar:
            return leer_lista(lista.pop(len(lista)-1),elemento_a_buscar)
        else: 
            return True

def main():
    leer_lista([0,1,2,3,4],2)

main()