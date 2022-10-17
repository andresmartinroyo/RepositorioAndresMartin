products = {
    "mobiles": {
        "Apple": [
            {
                "id": 1,
                "name": "iPhone 7",
                "price": 300
            },
            {
                "id": 2,
                "name": "iPhone 8",
                "price": 350
            },
            {
                "id": 3,
                "name": "iPhone Xr",
                "price": 450
            },
            {
                "id": 4,
                "name": "iPhone Xs",
                "price": 460
            },
            {
                "id": 5,
                "name": "iPhone 11",
                "price": 900
            },
            {
                "id": 6,
                "name": "iPhone 12",
                "price": 1100
            },
            {
                "id": 7,
                "name": "iPhone 13",
                "price": 1300
            },
        ],
        "Samsung": [
            {
                "id": 8,
                "name": "Samsung Galaxy Beam",
                "price": 150
            },
            {
                "id": 9,
                "name": "Samsung Galaxy S6",
                "price": 200
            },
            {
                "id": 10,
                "name": "Samsung Galaxy S7",
                "price": 300
            },
        ],
        "Xiaomi": [
            {
                "id": 11,
                "name": "Xiaomi Redmi Note 8",
                "price": 250
            },
            {
                "id": 12,
                "name": "Xiaomi Redmi Note 8 Pro",
                "price": 300
            },
        ]
    },
    "laptops": {
        "DELL": [
            {
                "id": 13,
                "name": "Dell Inspiron 15",
                "price": 600
            },
            {
                "id": 14,
                "name": "Dell Latitude 14",
                "price": 650
            },
        ],
        "MAC": [
            {
                "id": 15,
                "name": "MacBook Pro 13",
                "price": 900
            },
            {
                "id": 16,
                "name": "MacBook M1",
                "price": 1500
            },
        ]
    },
}
while True:
    print("===========\n  Welcome\n===========")
    ans=input("¿Qué operación desea realizar?\n1.-Ver Inventario.\n2.-Registrar compra.\n3.-Salir.\n==> ")
    
    #Verificador de respuestas
    while ans.isalpha() and ans!="1" and ans!="2" and ans != "3":
        ans=input("\nInvalid option.\n¿Qué operación desea realizar?\n1.-Ver Inventario.\n2.-Registrar compra.\n3.-Salir.\n==>")
    
    if ans=="1":
        for clase, marca in products.items():
            print(clase)
            for nombre, lista_products in marca.items():
                print(nombre)
                for producto in lista_products:
                    print("ID {}, Nombre {} and price {}.".format(producto["id"], producto["name"], producto["price"]))

    elif ans=="2":
        Nombre=input("\n Ingrese el nombre del cliente. \n\n==>")
        DNI=input("\n Ingrese el DNI del cliente. \n\n==>")
        compra=input("\n Ingrese el ID del producto que desea comprar. \n\n==>")
        cliente={}
        cliente["Nombre"]=Nombre
        cliente["DNI"]=DNI
        cliente["compra"]=compra
        for clase, marca in products.items():
            for nombre, lista_products in marca.items():
                for producto in lista_products:
                    if producto.get("id")==int(compra):
                        if producto.get("name").isalpha():
                            print("El cliente {}, de DNI {}, ha comprado {} al precio de {}".format(cliente["Nombre"],cliente["DNI"], producto.get("name"), producto.get("price")) )
                        else:

                            #PROMOCION
                            precio_descuento=producto.get("price")*0.8
                            print("El cliente {}, de DNI {}, ha comprado {} al precio {} que con un descuento de 20 por ciento, queda un precio total de {}".format(cliente["Nombre"],cliente["DNI"], producto.get("name"), producto.get("price"), precio_descuento) )
                            break



    elif ans == "3":
        break
