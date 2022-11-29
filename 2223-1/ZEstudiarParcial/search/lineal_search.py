def lineal_search(lista,numero):
    for n in lista:
        if n==numero:
            return True
        
if lineal_search([6 ,5 ,3,1,8,7,2,4],9):
    print("El numero esta")
else:
    print("El numero no esta")