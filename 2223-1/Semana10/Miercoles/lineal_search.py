def lineal_search(number,lista):
    for n in lista:
        if n == number:
            return number
        
def main():
    lista=[6 ,5 ,3,1,8,7,2,4]
    number = int(input("Insert a number: "))
    if lineal_search(number,lista):
        print(f"El numero {number} está en la lista.")
    else:
        print(f"El numero {number} no está en la lista.")
    
main()
