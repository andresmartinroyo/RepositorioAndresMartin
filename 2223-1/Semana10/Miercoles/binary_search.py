#Elementos tienen que estar ordenados 

def binary_search(lista,number):
    start=0
    final = len(lista)-1
    middle = (start + final)//2
    if len(lista)==1:
        if lista[0]==number:
            return number
        else :
            return -1

    if number > lista[middle]:
        return binary_search(lista[middle:final],number)

    elif number < lista[middle]:
        return binary_search(lista[start:middle],number)
    else: 
        return binary_search(lista[middle],number)

def main():
    lista = [1,2,3,4,5,6,7,8,9]
    number = int(input("Insert a number: "))
    if binary_search(lista,number):
        print(f"El numero {number} está en la lista.")
    else:
        print(f"El numero {number} no está en la lista.")

main()
    