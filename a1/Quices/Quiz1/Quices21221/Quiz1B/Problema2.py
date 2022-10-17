info = {
    "shirt_sizes": ["XXS", "XS", "S", "M", "L", "XL", "XXL"],
    "colors": {
        "plain": "white,black,blue,gray",
        "tie-dye": "rainbow,acid wash"
    },
    "print_sizes": [[(10, 10), 12.30], [(20, 15), 14.60]]
}
buyerspurchases={}
cont=0
payments_costumer={}
while True:
    ans=input("What would you like to do?\n1.-Register purchase.\n2.-See purchases history.\n3.-Exit.\n==>")
    while ans.isalpha():
        ans=input("Invalid answer. Please register an accepted answer\nWhat would you like to do?\n1.-Register purchase.\n2.-See purchases history.\n3.-Exit.\n==>")
    ans=int(ans)
    if ans==1:
        buyerdata={}
        #Data y verificadores.

        #ID

        buyerdata["ID"]=input("Introduce el ID del comprador.\n")
        while buyerdata["ID"].isalpha():
            buyerdata["ID"]=input("Error. Reingresar datos.\n")

        #Talla

        buyerdata["Talla"]=input("Introduce la talla del comprador.\n")
        while buyerdata["Talla"].isnumeric():
            buyerdata["Talla"]=input("Error. Reingresar datos.\n")
        
        #Color

        buyerdata["Color"]=input("Introduce el color de la camisa del comprador.\n")
        while buyerdata["Talla"].isnumeric():
            buyerdata["Talla"]=input("Error. Reingresar datos.\n")

        #Tamaño estampado

        buyerdata["Tamaño estampado"]=input("Introduce el tamaño del estampado de la camisa del comprador.\n")
        
        while buyerdata["Tamaño estampado"].isalpha():
            buyerdata["Tamaño estampado"]=input("Error. Reingresar datos.\n")
        if buyerdata["Tamaño estampado"]=="1":
            buyerdata["Tamaño estamapdo"]=(10, 10)
            payments_costumer[ buyerdata["ID"]]= 12.30
        elif buyerdata["Tamaño estampado"]=="2":
            buyerdata["Tamaño estamapdo"]=(10, 15)
            payments_costumer[ buyerdata["ID"]]=14.6
        

        
        #Rellenar diccionario
        
        buyerspurchases[cont]=buyerdata
        cont+=1
        
        #Bono Palindromo

        dni=buyerdata["ID"]    
        if dni==dni[::-1]:
            print("El cliente obtiene un descuento")


    elif ans==2:
        for purchases, value in buyerspurchases.items():
            print("El comprador identificado como {} ha realizado una compra de una camisa de talla {}, color {} y con un estampado de tamaño {}.".format( value["ID"], value["Talla"], value["Color"], value["Tamaño estampado"]))
    elif ans==3:
        print("Reinicio de software.")
        break
    else:
        print("Acción no reconocida.")
        

