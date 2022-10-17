from pydoc import cli


def pedir_cedula():
    while True:
        try:
            cedula_cliente=int(input("Ingrese el número de cédula: "))
            return cedula_cliente
        except:
            print("Error, introduzca solo valores númericos.")
    
def pedir_tipo_de_vehiculo():
    while True:
        try:
            tipo_vehiculo_cliente=int(input("Introduzca el tipo del vehiculo del clietne:\n1.-Automático.\n2.-Sincrónico.\n==>"))
            if tipo_vehiculo_cliente==1:
                return "A"
            elif tipo_vehiculo_cliente==2:
                return "S"
            else:
                raise Exception
        except:
            print("Introduzca un dato válido.")

def numero_de_horas(cliente):
    while True:
        try:
            horas_cliente=int(input("Introduzca el número de horas que va a tomar el cliente: "))
            if cliente["Tipo de vehículo"]=="A":
                costo=horas_cliente*2500
            elif cliente["Tipo de vehículo"]=="S":
                costo=horas_cliente*3500
            
            costo_descuento=costo
            if horas_cliente>=3:
                costo_descuento=costo*0.85
            return costo, costo_descuento
        except:
            print("Introduzca un valor numérico.")
            
def contar_clientes(clientes):
    numero=0
    for id,cliente in clientes.items():
        numero=id
    print(f"Han habido {numero} clientes.")

def contar_clientes_por_tipo(clientes):
    carro_a=0
    carro_s=0
    for id,cliente in clientes.items():
        if clientes[id]["Tipo de vehículo"]=="A":
            carro_a+=1
        else:
            carro_s+=1
    print(f"Han habido {carro_a} clientes con carro automático y {carro_s} clientes con carro sincronico")

def contar_clientes_con_descuento(clientes):
    clientes_descontados=0
    for id,cliente in clientes.items():
        if clientes[id]["preciobruto"]!=clientes[id]["precioneto"]:
            clientes_descontados+=1
    print(f"El numero de clientes con descuento es {clientes_descontados}.")

def promedio_de_facturacion_por_tipo(clientes):
    carro_a=0
    carro_s=0
    contador_ganancias_a=0
    contador_ganancias_s=0
    for id,cliente in clientes.items():
        if clientes[id]["Tipo de vehículo"]=="A":
            carro_a+=1
            contador_ganancias_a+=clientes[id]["precioneto"]
        elif clientes[id]["Tipo de vehículo"]=="S":
            carro_s+=1
            contador_ganancias_s+=clientes[id]["precioneto"]
        promedio_a=carro_a/contador_ganancias_a
        promedio_s=carro_s/contador_ganancias_s
        print(f"En promedio, cada cliente de automatico gasta Bs.{promedio_a} y cada cliente de sincronico Bs.{promedio_s}.")

def main():
    print("***********Bienvendio a la escuela La Rápida***********")
    id_cliente=1
    clientes={}
    while True:
        try: 
            respuesta=int(input("¿Que desea hacer a continuación?\n1.-Registrar cliente.\n2.-Mostrar estadísticas.\n==>"))
            if respuesta == 1:
                cliente={}
                cliente["Cédula"]=pedir_cedula()
                cliente["Tipo de vehículo"]=pedir_tipo_de_vehiculo()
                cliente["preciobruto"],cliente["precioneto"]=numero_de_horas(cliente)
                clientes[id_cliente]=cliente
                id_cliente+=1
                print("************Factura**************")
                if cliente["preciobruto"]==cliente["precioneto"]:
                    print("El cliente de cédula {}, por lecciones en manejo de carro tipo {}, pagara un total de {}".format(cliente["Cédula"],cliente["Tipo de vehículo"],cliente["precioneto"])) 
                else :
                    print("El cliente de cédula {}, por lecciones en manejo de carro tipo {}, se la ha descontado un 15% de {} y pagará un total de {}".format(cliente["Cédula"],cliente["Tipo de vehículo"],cliente["preciobruto"],cliente["precioneto"])) 
            elif respuesta==2:
                contar_clientes(clientes)
                contar_clientes_por_tipo(clientes)
                contar_clientes_con_descuento(clientes)
                promedio_de_facturacion_por_tipo(clientes) #buggaido por que?
            else:
                raise Exception
        except:
            print("Ha habido un error en main")

main()