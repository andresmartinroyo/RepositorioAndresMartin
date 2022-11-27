import matplotlib.pyplot as plt
from collections import Counter

from Clases.Partidos import Partidos
from Clases.Clientes import Clientes
from Clases.Restaurantes import Restaurantes
from Clases.Estadios import Estadios




def promedio_de_gastos_en_los_vip():
    #recorre la lista de clientes y divide los castos aumulados entre la cantidad de vips
    numero_de_vip = 0
    acumulacion_de_gastos = 0
    for cliente in Clientes.clientes:
        if cliente.importancia == "VIP":
            numero_de_vip+=1
            #if cliente.total_total == None:
                #cliente.total_total = 120*1.16
            acumulacion_de_gastos+=cliente.total_total
    
    if numero_de_vip!=0:

        print(f"El promedio de gasto de los clientes VIP es de {acumulacion_de_gastos/numero_de_vip} unidades montarias/cliente. ")


def tabla_de_asistencia():
    x=[]
    y=[]
    for partido in Partidos.partidos:
        for estadio in Estadios.estadios:
            if estadio.id_estadio==partido.id_estadio:
                if len(partido.codigos_asignados)!=0:
                    x.append(partido.asistencia_total)
                    #necesito entender la 3 para seguir. LISTO
                    partido.contar_ventas()
                    datos=[partido.equipo_local,partido.equipo_visitante,estadio.nombre,partido.asistencia_total]
                    if partido.ventas_total != 0:
                        datos.append(partido.asistencia_total/partido.ventas_total)
                    y.append(datos)
    
    x_ordenada=[]
    y_ordenada=[]
    longitud=len(x)

    iteracion=0
    while iteracion<longitud:
        valor_minimo=min(x)
        indice_valor_minimo=x.index(valor_minimo)
        x_ordenada.append(x[indice_valor_minimo])
        y_ordenada.append(y[indice_valor_minimo])
        x.pop(indice_valor_minimo)
        y.pop(indice_valor_minimo)
        iteracion+=1
    label=[]
    for i in y_ordenada:
        juego=f"{i[0]}\n  vs  \n{i[1]}\n{i[2]}\nAsist: {i[3]}\nRatio asist: {i[4]}"
        label.append(juego)
    plt.bar(label[::-1], x_ordenada[::-1], color="purple")
    plt.show()

    return x_ordenada,y_ordenada


def partido_con_mas_asistencias(lista1,lista2):
    mayor_numero_de_asistencias=max(lista1)
    print("")
    print("Partido(s) con mas asistencias:")
    for indice in range(len(lista1)):
        if mayor_numero_de_asistencias==lista1[indice]:
            print(f"\t El partido de {lista2[indice][0]} vs {lista2[indice][1]}")


def partido_con_mas_ventas():
    max_ventas=0
    id_mas_ventas = None
    for partido in Partidos.partidos:
        if partido.ventas_total > max_ventas:
            id_mas_ventas=partido.id_partido
            max_ventas=len(partido.codigos_asignados)
    
    for partido in Partidos.partidos:
        if partido.id_partido == id_mas_ventas:
            print("")
            print(f"El partido {partido.equipo_local} vs {partido.equipo_visitante} con {max_ventas} entradas vendidas, fue el que mas entradas vendió.")


def producto_mas_vendido_por_restaurante():
    print("")
    for restaurante in Restaurantes.restaurantes:


        contador = Counter(restaurante.ventas)
        los_mas_repetidos = contador.most_common(3)

        if len(los_mas_repetidos):

            print(f"En {restaurante.nombre}: \n")

            for i in los_mas_repetidos:
                print(f"\t Se vendieron {i[1]} unidades de {i[0]} ")

def top_3_clientes():
    top_clientes={}
    for cliente in Clientes.clientes:
        if top_clientes.get(f"{cliente.nombre}{cliente.DNI}") == None:
            top_clientes[f"{cliente.nombre}{cliente.DNI}"]=1
        else: 
            top_clientes[f"{cliente.nombre}{cliente.DNI}"]+=1
    
    contador = Counter(top_clientes)
    los_mas_repetidos = contador.most_common(3)

    if len(los_mas_repetidos):
        print("")
        print("Los top clientes han sido:")
        for i in los_mas_repetidos:
            print(f"\t Se vendieron {i[0]} unidades de {i[1]} ")
