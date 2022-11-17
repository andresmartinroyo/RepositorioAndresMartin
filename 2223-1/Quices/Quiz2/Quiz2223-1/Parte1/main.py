from Refresco import Refresco
from Alcohol import Alcohol
from Bebidas import Bebidas

def mostrar_todo():
    cont=1
    for objeto in Bebidas.bebidas_bonito:
        
        print("")
        print("Numero: ", cont)
        print("Tipo de Bebida: ", objeto.tipo_de_bebida)
        objeto.mostrar()
        
        cont += 1

    print("")
        
            


def main():


    print("\nBienvenido al sistema.\n")

    #Pasar diccionario a lista de objetos
    almacen_desactualizado = {
            "Alcohol":
        [
        	{ "nombre": "Linaje", "marca": "Santa Teresa", "grado": 40, "tipo": "Ron", "disponible": True },
        	{ "nombre": "Black Label 18", "marca": "Jonnie Walker", "grado": 43, "tipo": "Whisky", "disponible": True },
        	{ "nombre": "Solera Verde", "marca": "Polar", "grado": 6, "tipo": "Cerveza", "disponible": True }
        ],
    
        "Refresco":
        [
        	{ "nombre": "Maltin Polar", "marca": "Polar", "azucar": 7, "sabor": "Malta", "disponible": True },
        	{ "nombre": "Pepsi", "marca": "Pepsico", "azucar": 7, "sabor": "Cola", "disponible": True },
        	{ "nombre": "Chinoto", "marca": "The Coca-Cola Company", "azucar": 4, "sabor": "Limon", "disponible": True }
        ] 
}

    for tipo_de_bebida, bebidas in almacen_desactualizado.items():

        if tipo_de_bebida == "Alcohol":

            for bebida in bebidas:

                cosa1 = Alcohol()
                cosa1.agregar_bebidas(bebida)
                Bebidas.bebidas_bonito.append(cosa1)


        elif tipo_de_bebida == "Refresco":
            
            for bebida in bebidas:

                cosa1 = Refresco()
                cosa1.agregar_bebidas(bebida)
                Bebidas.bebidas_bonito.append(cosa1)


        

    while True: 

        respuesta_1 = int(input("Introduce la opcion que deseas hacer a continuación:\n1.Ver inventario.\n2.Eliminar producto.\n3.Ver stats\n==>"))

        if respuesta_1==1:

            mostrar_todo()

        elif respuesta_1==2:

            try:

                respuesta_2= int(input("\nIntroduce el numero de la bebida que deseas borrar: "))

                Bebidas.bebidas_bonito[respuesta_2-1].cambiar_disponibilidad()
            
            except:

                print("\nHermano, pon un numero bien.\n")
        
            print("")

        elif respuesta_1==3:

            mayor_c_azucar=0
            mayor_azucar=""

            mayor_c_alcohol=0
            mayor_alcohol=""

            marcas_comunes={}

            for objeto in Bebidas.bebidas_bonito:

                if objeto.tipo_de_bebida=="Refresco":
                    if objeto.azucar > mayor_c_azucar:
                        mayor_azucar=objeto.nombre
                        mayor_c_azucar=objeto.azucar
                
                elif objeto.tipo_de_bebida=="Alcohol":
                    if objeto.grado > mayor_c_alcohol:
                        mayor_alcohol=objeto.nombre
                        mayor_c_alcohol=objeto.grado
                
                if marcas_comunes.get(objeto.marca)==None:
                    marcas_comunes[objeto.marca]=1

                else: 
                    marcas_comunes[objeto.marca]+=1

                    
                
            print("")
            print(f"El alcohol con más grado es, {mayor_alcohol}, y tiene un grado de {mayor_c_alcohol}")
            print(f"El refresco con más azucar es, {mayor_azucar}, y tiene una cantidad de {mayor_c_azucar}")

            for marcas, numero_de_productos in marcas_comunes.items():

                if numero_de_productos>1:
                    print(f"La marca {marcas} tiene {numero_de_productos} productos")
            
            print("")
        
            




main()
