medications = {
    "prescription": {
        "antibiotics": {
            "skin": [
                {
                    "id": 1,
                    "name": "Clindamicine",
                    "price": 300
                },
                {
                    "id": 2,
                    "name": "Cefadroxil",
                    "price": 350
                },
                {
                    "id": 3,
                    "name": "Amoxicillin",
                    "price": 320
                }
            ],
            "respiratory-system":[
                {
                    "id": 4,
                    "name": "Citromicine",
                    "price": 380
                },
                {
                    "id": 5,
                    "name": "Levofloxacine",
                    "price": 125
                },
                {
                    "id": 6,
                    "name": "Azitromicine",
                    "price": 740
                }
            ]
        },
        "analgesic": {
            "anti-inflammatories": [
                {
                    "id": 7,
                    "name": "HYDROCODONE-IBUPROFEN",
                    "price": 150
                },
                {
                    "id": 8,
                    "name": "IBUDONE",
                    "price": 180
                }
            ]
        }
    },
    "non-prescription": {
        "analgesic": {
            "general": [
                {
                    "id": 9,
                    "name": "Acetaminophen",
                    "price": 15
                },
                {
                    "id": 10,
                    "name": "Ibuprofen",
                    "price": 20
                }
            ]
        },
        "antihistamine": {
            "antiallergic": [
                {
                    "id": 11,
                    "name": "Loratadine",
                    "price": 12
                },
                {
                    "id": 12,
                    "name": "Desler M",
                    "price": 8
                },
                {
                    "id": 13,
                    "name": "Allegra",
                    "price": 21
                },
                {
                    "id": 14,
                    "name": "Fexofenadine",
                    "price": 18
                }
            ]
        }
    }
}

while True:
    Zozaya=True
    ans=input("Introduce la opcion que desea:\n1.- Ver inventario.\n2.- Registrar compra.\n==>")
    ans=int(ans)
    if ans==1:
        for type,medicamento in medications.items():
            print(f"\nDe tipo {type}:\n")
            for key1,lugar_del_cuerpo in medicamento.items():
                print(f"\tDe denominacion {key1}:\n ")
                for key2,lista in lugar_del_cuerpo.items():
                    print(f"\t\tPara {key2}:\n")
                    for i in range(len(lista)):
                        print("\t\t\tEl producto {}, con id {}, con un precio de {}." .format(lista[i].get("name"),lista[i].get("id"),lista[i].get("price")))
                    print("")
    elif ans==2:
        cliente={}
        cliente["Nombre"]=input("Insterte el nombre del cliente: ")
        while cliente["Nombre"].isnumeric():
            cliente["Nombre"]=input("Insterte el nombre del cliente: ")
        
        cliente["Apellido"]=input("Insterte el apellido del cliente: ")
        while cliente["Apellido"].isnumeric():
            cliente["Apellido"]=input("Insterte el apellido del cliente: ")
        
        cliente["DNI"]=input("Insterte el DNI del cliente: ")
        while cliente["DNI"].isalpha():
            cliente["DNI"]=input("Insterte el DNI del cliente: ")
        
        #BONO
        ultimos_3=""
        for i in range(-3,0):
            ultimos_3+=(cliente["DNI"][i])
            m=int(ultimos_3)
            aux=m-1
            while aux>1 and m!=2:
                if m%aux!=0:
                    aux-=1
                if m==2 or m%aux==0:
                    Zozaya=False
                    break 

        

        print(ultimos_3)
        cliente["id"]=input("Insterte el id de las pastillas que quiere comprar el cliente: ")
        while cliente["id"].isalpha():
            cliente["id"]=input("Insterte el id de las pastillas que quiere comprar el cliente: ")
        
        print("\t\t************FACTURA************")
        for type,medicamento in medications.items():
            for key1,lugar_del_cuerpo in medicamento.items():
                for key2,lista in lugar_del_cuerpo.items():
                    for i in range(len(lista)):
                        if lista[i]["id"]==int(cliente["id"]) and Zozaya==False:
                            precio_nuevo=lista[i].get("price")*0.6
                            print("El cliente {} {}, DNI {}, ha copmprado el medicamento {} a un precio de {}.".format(cliente["Nombre"],cliente["Apellido"],cliente["DNI"],lista[i].get("name"),precio_nuevo))
                        elif lista[i]["id"]==int(cliente["id"]) and Zozaya==True:
                            print("El cliente {} {}, DNI {}, ha copmprado el medicamento {} a un precio de {}.".format(cliente["Nombre"],cliente["Apellido"],cliente["DNI"],lista[i].get("name"),lista[i].get("price")))
    elif ans==3:
        break