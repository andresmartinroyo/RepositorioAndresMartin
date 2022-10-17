def primicidad(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def main():
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

    clientes={}
    id_cliente=1
    stat_juegos={}

    while True: 
        while True:
            ans=input("¿Qué desea hacer a continuación?\n1.-Ver juegos.\n2.-Registrar compra.\n3.-Ver stats.\n4.-Salir.\n==>")
            if ans.isnumeric():
                ans=int(ans)
                break
        if ans==1:
            for clasificacion,games in juegos.items():
                print(f"Juegos tipo {clasificacion}:")
                for juego in games:
                    print("\tJuego:", juego["name"])
                    print("\tID:", juego["id"])
                    if juego["price"]==0:
                        print("\tPrecio: Es gratis")
                    else:
                        print("\tPrecio:", juego["price"])
                    print("")
                print("")
        if ans==2:

            cliente={}
            while True: 
                cliente["Nombre"]=input("Introduce el nombre del cliente: ")
                if cliente["Nombre"].isalpha():
                    break
            while True: 
                cliente["Apellido"]=input("Introduce el apellido del cliente: ")
                if cliente["Apellido"].isalpha():
                    break
            while True: 
                cliente["Cedula"]=input("Introduce la cedula del cliente: ")
                if cliente["Cedula"].isnumeric():
                    break
            while True: 
                cliente["id"]=input("Introduce el id del juego del cliente: ")
                if cliente["id"].isnumeric():
                    break
            
            for clasificacion,games in juegos.items():
                for juego in games:
                    if juego["id"]==int(cliente["id"]):
                        precio=juego["price"]
                        cliente["Juego"]=juego["name"]

            descuento=0
            if primicidad(int(cliente["Cedula"][-3::])):
                descuento=precio*0.4
            
            print("**********FACTURA***********")
            print("CLiente: {} {}".format(cliente["Nombre"], cliente["Apellido"]))
            print("Cedula: {}".format(cliente["Cedula"]))
            print("Juego: {}".format(cliente["Juego"]))
            if precio == 0: 
                print("Sin costo")
            elif precio >0:
                total=precio-descuento
                print("Subtotal: {}".format(precio))
                print("Total: {}".format(total))
            
            clientes[id_cliente]=cliente
            id_cliente+=1

            if cliente["Juego"] in stat_juegos:
                stat_juegos[cliente["Juego"]]+=1
            else:
                stat_juegos[cliente["Juego"]]=1

        if ans==3:
            max_juego=""
            max_compra=0
            for juegos_comprados,cantidad_de_compras in stat_juegos.items():
                if cantidad_de_compras>0:
                        max_juego=juegos_comprados
                        max_compra=cantidad_de_compras
            print(f"Juego más vendido: {max_juego}")
            print(f"Cantidad de ventas: {max_compra}")
        if ans==4:
            break


main()