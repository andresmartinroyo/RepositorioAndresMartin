juegos = {
    "Shooter": [
        {
            "id": 1,
            "name": "Overwatch2",
            "price": 60  
        },
        {
            "id": 2,
            "name": "Valorant",
            "price": 0
        },
        {
            "id": 3,
            "name": "Pixel Gun 3D",
            "price": 10
        }
    ],
    "RPG": [
        {
            "id": 4,
            "name": "Pokemon",
            "price": 50  
        },
        {
            "id": 5,
            "name": "Final Fantasy Exvius",
            "price": 0
        }
    ],
    "Open World": [
        {
            "id": 6,
            "name": "Minecraft",
            "price": 60  
        },
        {
            "id": 7,
            "name": "Cyberpunk 2077",
            "price": 60
        },
        {
            "id": 8,
            "name": "GTA V",
            "price": 40
        }
    ],  
}
cont1=1
clientes={}
print("\nBienvenido a nuestra tienda de videojugos.\n")
while True:
    Zozaya=True
    ans=input("\nSelccione la opcion que se ajuste a lo que desea realizar a continuación:\n1.-Ver catálogo.\n2.-Registrar compra.\n3.-Ver clientes y estadísticas.\n4.- Salir.\n==> ")
    #Verificar
    while ans.isalpha():
        ans=input("\nSelccione la opcion que se ajuste a lo que desea realizar a continuación:\n1.-Ver catálogo.\n2.-Registrar compra.\n3.-Ver clientes y estadísticas.\n4.- Salir.\n==> ")

    ans=int(ans)


    #Si ans es 1
    if ans==1:
        for categoria, lista in juegos.items():
            print(f"Disponmeos de los siguientes juegos la categoria {categoria}:")
            for juego in lista:
                if juego["price"]!=0:
                    print("El juego {} con el id {} a un precio de {}.".format(juego["name"],juego["id"],juego["price"]))
                else:
                    print("El juego {} con el id {} gratiuto.".format(juego["name"],juego["id"]))
            print("")
    
    #Si ans es 2
    elif ans == 2:
        cliente={}
        cliente["Nombre"]=input("Introduce el nombre del cliente: ")
        #VERIFICAR
        while cliente["Nombre"].isnumeric():
            cliente["Nombre"]=input("Introduce el id del juego que el cliente desea comprar: ")

        cliente["Apellido"]=input("Introduce el apellido del cliente: ")
        #Verificar
        while cliente["Apellido"].isnumeric():
            cliente["Apellido"]=input("Introduce el id del juego que el cliente desea comprar: ")

        cliente["DNI"]=input("Introduce el DNI del cliente: ")
        #Verificar
        while cliente["DNI"].isalpha():
            cliente["DNI"]=input("Introduce el id del juego que el cliente desea comprar: ")

        #BONO
        numero_entero=""
        for digito in range(3-len(cliente["DNI"]),len(cliente["DNI"]),1):
            numero_entero+=cliente["DNI"][digito]
        numero_entero=int(numero_entero)
        cont = numero_entero-1
        if numero_entero>=2:
            while numero_entero % cont != 0: 
                cont = cont - 1
                if cont == 1:
                    break
            if numero_entero % cont == 0 and cont != 1 :
                pass
            else:
                Zozaya=False

        cliente["id"]=input("Introduce el id del juego que el cliente desea comprar: ")
        #Verificar
        while cliente["id"].isalpha():
            cliente["id"]=input("Introduce el id del juego que el cliente desea comprar: ")

        cliente["id"]=int(cliente["id"])



        print("\n")
        for categoria, lista in juegos.items():
            for juego in lista:
                if juego["id"]==cliente["id"]:

                    #Bono 
                    cliente["Precio"]=juego["price"]
                    cliente["Juego"]=juego["name"]
        
                    if Zozaya==False:
                        cliente["Precio"]=0.6*cliente["Precio"]
                    if juego["price"]!=0:
                        print("El cliente {} {} de DNI {} ha adquirido el juego a un precio de {}. ".format(cliente["Nombre"],cliente["Apellido"],cliente["Juego"], cliente["Precio"]))
                    else:
                        print("El cliente {} {} de DNI {} ha adquirido el juego gratis. ".format(cliente["Nombre"],cliente["Apellido"],juego["name"]))
                    break
                    
        clientes[cont1]=cliente
        cont1+=1
    
    #Si ans es 3
    elif ans==3:
        for numero,usuario in clientes.items():
            print("Cliente {}, nombre {}, apellido {}, DNI {}, compro el juego {} ".format(numero,usuario["Nombre"],usuario["Apellido"], usuario["DNI"], usuario["Juego"]))

    elif ans==4:
        break

    else :
        pass