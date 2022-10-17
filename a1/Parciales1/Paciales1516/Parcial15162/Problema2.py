def pedir_cedula():
    while True:
        cedula_cliente=input("Introduce la cédula del cliente: ")
        if cedula_cliente.isnumeric():
            break
    return cedula_cliente

def pedir_edad():
    while True:
        edad_cliente=input("Introduce la edad del cliente: ")
        if edad_cliente.isnumeric():
            break
    return int(edad_cliente)

def pedir_sexo():
    while True:
        sexo_cliente=input("Introduce el genero del cliente.\nM.-Masculino\nF.-Femenino\n==>").title()
        if sexo_cliente=="M" or sexo_cliente=="F":
            break
    return sexo_cliente

def pedir_tipo_de_estudio():
    estudios=["U","T","R"]
    while True:
        tipo_cliente=input("Introduce el tipo de estudio.\nU.-Ultrasonido\nT.-Tomografía\nR.-Radiografía\n==>").title()
        if tipo_cliente in estudios:
            break
    return tipo_cliente

def pedir_dinero(cliente,id_cliente):
    if cliente["Estudio"]=="U":
        preciobruto=8900
    elif cliente["Estudio"]=="T":
        preciobruto=12640
    elif cliente["Estudio"]=="R":
        preciobruto=15600
    precioneto=preciobruto*1
    if cliente["Sexo"]=="F" and cliente["Edad"]>55:
        precioneto=preciobruto*0.75
    elif cliente["Sexo"]=="M" and cliente["Edad"]>65:
        precioneto=preciobruto*0.75
    if id_cliente%2!=0:
        precioneto*=0.98
    return preciobruto,precioneto

def generar_factura(cliente,id_cliente):
    if cliente["Precio neto"]==cliente["Precio bruto"]:
        print("El cliente de cedula {}, sexo {}, edad {}, realizo el estudio {} y pagara {}".format(cliente["DNI"],cliente["Sexo"],cliente["Edad"],cliente["Estudio"],cliente["Precio neto"]))
    elif cliente["Precio neto"]!=cliente["Precio bruto"]:
        print("El cliente de cedula {}, sexo {}, edad {}, realizo el estudio {} y con el descuento pagara {}".format(cliente["DNI"],cliente["Sexo"],cliente["Edad"],cliente["Estudio"],cliente["Precio neto"]))

def contar_clientes(clientes):
    estudio_u=0
    estudio_t=0
    estudio_r=0
    for id,cliente in clientes.items():
        if clientes[id]["Estudio"]=="U":
            estudio_u+=1
        elif clientes[id]["Estudio"]=="T":
            estudio_t+=1
        elif clientes[id]["Estudio"]=="R":
            estudio_r+=1
    print(f"Hubo {estudio_u} ultrasonidos, {estudio_t} tomografías y {estudio_r} resonancias.")
    return estudio_r+estudio_t+estudio_u

def contar_descuentos(clientes):
    descuentos=0
    for id, cliente in clientes.items():
        if clientes[id]["Precio neto"]!=clientes[id]["Precio bruto"]:
            descuentos+=1
    print(f"Se realizaron {descuentos} descuentos.")

#Error
def contar_total(clientes):
    Total=0
    for id, cliente in clientes.items():
        Total=+clientes[id]["Precio neto"]
    print(f"Hoy se facturó {Total}")
    return Total

def promedio_cliente(Total,n):
    promedio=Total/n
    print(f"El promedio pro cliente es de {promedio}")

def main():
    clientes={}
    id_cliente=1
    while True:
        try:

            while True:
                respuesta=input("¿Qué desea hacer a continuación?\n1.-Registrar cliente.\n2.-Terminar día\n==>")
                if respuesta.isnumeric():
                    break
            if respuesta == "1":
                cliente={}
                cliente["DNI"]=pedir_cedula()
                cliente["Edad"]=pedir_edad()
                cliente["Sexo"]=pedir_sexo()
                cliente["Estudio"]=pedir_tipo_de_estudio()
                cliente["Precio bruto"],cliente["Precio neto"]=pedir_dinero(cliente,id_cliente)
                generar_factura(cliente,id_cliente)
                clientes[id_cliente]=cliente
                id_cliente+=1
            elif respuesta=="2":
                contar_descuentos(clientes)
                n=contar_clientes(clientes)
                Total=contar_total(clientes)
                promedio_cliente(Total,n)
                
        except:
            print("Eroor")

main()