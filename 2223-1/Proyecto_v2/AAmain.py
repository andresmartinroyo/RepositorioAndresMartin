#librerias
import requests
import json
import Estadistica.estadistica_del_programa as ptm

#Clases
from Clases.Equipos import Equipos
from Clases.Estadios import Estadios
from Clases.Partidos import Partidos
from Clases.Clientes import Clientes
from Clases.Restaurantes import Restaurantes
from Clases.Productos import Productos



#Funciones
def mostrar_equipos(equipos):
    for team in equipos:
        team.mostrar_equipo()


def mostrar_estadios(estadios):
    for estadio in estadios:
        estadio.mostrar_estadio()


def mostrar_partidos(partidos):
    for match in partidos:
        match.mostrar_partido()
    
def cargar_datos(ruta_estadios,ruta_partidos,ruta_clientes):
    with open(ruta_estadios) as f_estadios:
        dict_stadiums = json.load(f_estadios)
    with open(ruta_partidos) as f_partidos:
        dict_matches = json.load(f_partidos)
    with open(ruta_clientes) as f_clientes:
        dict_clients = json.load(f_clientes)
    return dict_stadiums,dict_matches,dict_clients




    


def main():

    dict_de_equipos= requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json").json()
    dict_clientes=None

    while True:
        respuesta=input("Que deseas:\n1. Cargar sesion. \n2. Empezar desde cero.\n==> ")
        if respuesta.isnumeric() and (int(respuesta)==1 or int(respuesta)==2):
            respuesta=int(respuesta)
            break

    if respuesta==2:
        dict_de_estadios= requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json").json()
        dict_de_partidos= requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json").json()

    else :
        dict_de_estadios,dict_de_partidos,dict_clientes=cargar_datos("Datos_estadios.json","Datos_partidos.json","Datos_clientes.json")
        

    for equipo in dict_de_equipos:
        team=Equipos()
        team.asignacion_de_datos(equipo)

        Equipos.equipos.append(team)
    

    for estadio in dict_de_estadios:
        stadium=Estadios()
        stadium.definir_estadios_restaurantes_productos(estadio)

        
        Estadios.estadios.append(stadium)

    for partido in dict_de_partidos:
        match=Partidos()
        match.definir_partidos(partido)

        Partidos.partidos.append(match)
    
    if dict_clientes!=None:
        for cliente in dict_clientes:
            client=Clientes()
            client.recordar_clientes(cliente)

            Clientes.clientes.append(client)


    while True:
        print("")
        while True:
            respuesta_1 = input("OPCIONES:\n1. Buscar Partidos.\n2. Comprar entrada.\n3. Asistencia a partidos.\n4. Ver productos en restaurantes\n5. Vender producto a cliente.\n6. Ver estadisticas.\n7. Guaradar datos.\n ==> ")
            if respuesta_1.isnumeric():
                respuesta_1=int(respuesta_1)
                break


        if respuesta_1 == 1:

            respuesta_1_1=int(input("Deseas buscar partidos por \n1. Por país.\n2. Por estadio.\n3. Por fecha.\n==> "))

            if respuesta_1_1 == 1:

                respuesta_1_1_1=input("Introduce el nombre de la seleccion que deseas ver: ").title()

                for partido in Partidos.partidos:
                    if respuesta_1_1_1 == partido.equipo_local or respuesta_1_1_1 == partido.equipo_visitante:
                        partido.mostrar_partido()
                    
            elif respuesta_1_1 == 2:
                
                mostrar_estadios(Estadios.estadios)
                respuesta_1_1_2 = int(input("Introduce el id del estadio del que deseas ver sus partidos: "))

                for partido in Partidos.partidos:
                    if respuesta_1_1_2 == partido.id_estadio:
                        partido.mostrar_partido()

            elif respuesta_1_1 == 3:

                respuesta_1_1_3 = input("Introduce la fecha en la cual quiere ver los partidos(mes/día/año): ")

                for partido in Partidos.partidos:
                    if respuesta_1_1_3 == partido.fecha:
                        partido.mostrar_partido()


        elif respuesta_1 == 2:

            print("")
            while True:
                respuesta_1_2 = input("Introuce el id del partido que deseas ver: ")
                if respuesta_1_2.isnumeric() and (int(respuesta_1_2)>0 and int(respuesta_1_2)<49 ):
                    break
                
            for partido in Partidos.partidos:
                if int(partido.id_partido)==respuesta_1_2:
                    partido.mostrar_disponibilidad_de_asientos(respuesta_1_2)
            cliente=Clientes()
            cliente.registrar_cliente(respuesta_1_2)
            Clientes.clientes.append(cliente)


        elif respuesta_1 == 3:

            print("")
            while True:
                respuesta_1_3_1 = input("Introduce el id del partido al que el cliente esta entrando: ")
                if respuesta_1_3_1.isnumeric() and (int(respuesta_1_3_1)>0 and int(respuesta_1_3_1)<49):
                    break
            while True:
                respuesta_1_3_2 = input("Introduce el numero del documento de identidad del cliente esta entrando: ")
                if respuesta_1_3_2.isnumeric():
                    break
            while True:
                respuesta_1_3_3 = input("Introduce el codigo del cliente esta entrando: ")
                if respuesta_1_3_3.isnumeric():
                    respuesta_1_3_3=int(respuesta_1_3_3)
                    break
            
            Osorio=False
            for cliente in Clientes.clientes:
                if cliente.id_partido == respuesta_1_3_1 and cliente.DNI == respuesta_1_3_2 and cliente.codigo == respuesta_1_3_3:
                    for partido in Partidos.partidos:
                        if partido.id_partido==cliente.id_partido:
                            if respuesta_1_3_3 not in partido.codigos_registrados:
                                partido.codigos_registrados.append(respuesta_1_3_3)
                                partido.asistencia_total += 1
                                print("")
                                print("Codigo confirmado")
                                Osorio=True
                                break
                            elif respuesta_1_3_3 in partido.codigos_registrados:
                                print("")
                                print("Este codigo ya ha sido registrado")
                                Osorio=True
            if Osorio== False:
                print("")
                print("No se encuentra registrado. Asegurate de marcar bien :)")
            

        elif respuesta_1 == 4:

            respuesta_1_4=input("Introduce por que metodo desea realizar la busqueda de productos: \n1.Nombre\n2.Tipo\n3.Rango de precio.\n==>")
            while respuesta_1_4.isalpha():
                print("")
                respuesta_1_4=input("Introduce por que metodo desea realizar la busqueda de productos: \n1.Nombre\n2.Tipo\n3.Rango de precio.\n==>")

            if respuesta_1_4 == "1":

                print("")
                respuesta_1_4_1 = input("Introduce el nombre de la comida que deseas buscar: ").title()

                #recorre productos y restaurtantes, si el id de los productos y el del restaurante es el mismo
                #y lo que el usuario pidio buscar es igual al atributo del producto se imprime
                for restaurante in Restaurantes.restaurantes:
                    for producto in Productos.productos[restaurante.id_restaurante]:
                            if producto.nombre==respuesta_1_4_1.title():
                                print("")
                                print(f"El restuarante {restaurante.nombre}, tiene:")
                                print("Nombre: ", producto.nombre)
                                print("Precio: ", producto.precio)
                                print("Tipo: ", producto.tipo)
                                if producto.tipo=="bebida":
                                    if producto.alcohol:
                                        print("Con alcohol")
                                    else:
                                        print("Sin alcohol")
                                elif producto.tipo=="comida":
                                    if producto.coccion:
                                        print("Comida preparada")
                                    else:
                                        print("De paquete")
                                print("Cantidad: ", producto.cantidad)
            
            if respuesta_1_4 == "2":

                print("")
                respuesta_1_4_2 = input("Introduce el tipo de la comida que deseas buscar: ").lower()

                #recorre productos y restaurtantes, si el id de los productos y el del restaurante es el mismo
                #y lo que el usuario pidio buscar es igual al atributo del producto se imprime
                for restaurante in Restaurantes.restaurantes:
                    for producto in Productos.productos[restaurante.id_restaurante]:
                            if producto.tipo==respuesta_1_4_2.lower():
                                print("")
                                print(f"El restuarante {restaurante.nombre}, tiene:")
                                print("Nombre: ", producto.nombre)
                                print("Precio: ", producto.precio)
                                print("Tipo: ", producto.tipo)
                                if producto.tipo=="bebida":
                                    if producto.alcohol:
                                        print("Con alcohol")
                                    else:
                                        print("Sin alcohol")
                                elif producto.tipo=="comida":
                                    if producto.coccion:
                                        print("Comida preparada")
                                    else:
                                        print("De paquete")
                                print("Cantidad: ", producto.cantidad)
    
            if respuesta_1_4 == "3":

                print("")

                #pido el valor minimio y maximo del precio del que quiere buscar y valido que sean numeros 
                respuesta_1_4_3_min = input("Introduce el precio mínimo: ")
                while respuesta_1_4_3_min.isalpha():
                    respuesta_1_4_3_min = input("Introduce el precio mínimo: ")
                respuesta_1_4_3_min=int(respuesta_1_4_3_min)
                
                respuesta_1_4_3_max = input("Introduce el precio máximo: ")
                while respuesta_1_4_3_max.isalpha():
                    respuesta_1_4_3_max = input("Introduce el precio máximo: ")
                respuesta_1_4_3_max=int(respuesta_1_4_3_max)

                #recorre productos y restaurtantes, si el id de los productos y el del restaurante es el mismo
                #y lo que el usuario pidio buscar es igual al atributo del producto se imprime
                for restaurante in Restaurantes.restaurantes:
                    for producto in Productos.productos[restaurante.id_restaurante]:
                            if producto.precio<=respuesta_1_4_3_max and producto.precio>=respuesta_1_4_3_min:
                                print("")
                                print(f"El restuarante {restaurante.nombre}, tiene:")
                                print("Nombre: ", producto.nombre)
                                print("Precio: ", producto.precio)
                                print("Tipo: ", producto.tipo)
                                if producto.tipo=="bebida":
                                    if producto.alcohol:
                                        print("Con alcohol")
                                    else:
                                        print("Sin alcohol")
                                elif producto.tipo=="comida":
                                    if producto.coccion:
                                        print("Comida preparada")
                                    else:
                                        print("De paquete")
                                print("Cantidad: ", producto.cantidad)

            print("")

            
        elif respuesta_1 == 5:

            print("")
            print("Con que quieres comprar en nuestro restaurante... veamos si eres digno.")

            respuesta_1_5=input("Introduce tu cedula: ")
            while respuesta_1_5.isalpha():
                print("")
                respuesta_1_5=input("Introduce tu cedula: ")

            Osorio=False
            for cliente in Clientes.clientes: 
                if cliente.importancia=="VIP" and cliente.total != 0:
                    if cliente.DNI==respuesta_1_5:
                        Osorio=True
                        cliente_que_comprara=cliente
                        break

            if Osorio == True:

                print("")
                print("Bienvenido guapx")          
                cliente_que_comprara.registrar_compra_restaurante()          

            elif Osorio == False:
                
                print("")
                print("No le den nada a este pobre")


        elif respuesta_1 == 6:
            

            print("")
            ptm.promedio_de_gastos_en_los_vip()
            lista1,lista2=ptm.tabla_de_asistencia()
            ptm.partido_con_mas_asistencias(lista1,lista2)
            ptm.partido_con_mas_ventas()
            ptm.producto_mas_vendido_por_restaurante()
            ptm.top_3_clientes()

                        
        elif respuesta_1 == 7:

            print("")
            datos_estadios=[]
            
            for estadio in Estadios.estadios:
                dict_de_estadios={}
                dict_de_estadios["id"]=estadio.id_estadio
                dict_de_estadios["name"]=estadio.nombre
                dict_de_estadios["capacity"]=estadio.asientos
                dict_de_estadios["location"]=estadio.localizacion
                dict_de_estadios["restaurants"]=[]
                for restaurante in Restaurantes.restaurantes:
                    if restaurante.id_estadio == estadio.id_estadio:
                        local={}
                        local["name"]=restaurante.nombre
                        local["products"]=[]
                        for numero_restaurante , items in Productos.productos.items():
                            if numero_restaurante==restaurante.id_restaurante:
                                for product in items:
                                    cosas={}
                                    cosas["name"]=product.nombre
                                    cosas["quantity"]=product.cantidad
                                    cosas["price"]=product.precio
                                    if product.tipo=="comida":
                                        cosas["type"]="food"
                                        if product.coccion == True:
                                            cosas["adicional"]= "plate"
                                        else:
                                            cosas["adicional"]= "package"
                                    if product.tipo=="bebida":
                                        cosas["type"]="beverages"
                                        if product.alcohol == True:
                                            cosas["adicional"]= "alcoholic"
                                        else:
                                            cosas["adicional"]= "non-alcoholic"
                                    local["products"].append(cosas)
                        dict_de_estadios["restaurants"].append(local)
                datos_estadios.append(dict_de_estadios)
            with open("Datos_estadios.json","w") as f:
                json.dump(datos_estadios, f)

                
            datos_partidos=[]
            for partido in Partidos.partidos:
                dict_de_partidos={}
                dict_de_partidos["home_team"]=partido.equipo_local
                dict_de_partidos["away_team"]=partido.equipo_visitante
                dict_de_partidos["date"]=f"{partido.fecha} {partido.hora}"
                dict_de_partidos["stadium_id"]=partido.id_estadio
                dict_de_partidos["id"]=partido.id_partido
                dict_de_partidos["disponiblidad de asientos"]=partido.disponibilidad_de_asientos
                dict_de_partidos["canitidad de asientos"]=partido.cantidad_de_asientos
                dict_de_partidos["codigos totales"]=partido.codigos_totales
                dict_de_partidos["codigos asignados"]=partido.codigos_asignados
                dict_de_partidos["codigos registrados"]=partido.codigos_registrados
                dict_de_partidos["ventas total"]=partido.ventas_total
                dict_de_partidos["asistencia total"]=partido.asistencia_total
                datos_partidos.append(dict_de_partidos)
            with open("Datos_partidos.json","w") as f:
                json.dump(datos_partidos, f)          

            datos_clientes = []
            for cliente in Clientes.clientes:
                dict_clientes = {}
                dict_clientes["nombre"] = cliente.nombre
                dict_clientes["DNI"] = cliente.DNI
                dict_clientes["edad"] = cliente.edad
                dict_clientes["id_partido"] = cliente.id_partido
                dict_clientes["id_estadio"] = cliente.id_estadio
                dict_clientes["tipo_de_entrada"] = cliente.tipo_de_entrada
                dict_clientes["asiento"] = cliente.asiento
                dict_clientes["codigo"] = cliente.codigo
                dict_clientes["subtotal"] = cliente.subtotal
                dict_clientes["descuento"] = cliente.descuento
                dict_clientes["iva"] = cliente.iva
                dict_clientes["realizar_pago"] = cliente.realizar_pago
                dict_clientes["total"] = cliente.total
                dict_clientes["importancia"] = cliente.importancia
                dict_clientes["carrito"] = cliente.carrito
                dict_clientes["restaurante_del_que_puede_comprar"] = cliente.restaurante_del_que_puede_comprar
                dict_clientes["subtotal_restaurante"] = cliente.subtotal_restaurante
                dict_clientes["descuento_restaurante"] = cliente.descuento_restaurante
                dict_clientes["iva_restaurante"] = cliente.iva_restaurante
                dict_clientes["total_restaurante"] = cliente.total_restaurante
                dict_clientes["mayoria_de_edad"] = cliente.mayoria_de_edad
                dict_clientes["total_total"] = cliente.total_total
                datos_clientes.append(dict_clientes)
            with open("Datos_clientes.json","w") as f:
                json.dump(datos_clientes, f)

                            


main()