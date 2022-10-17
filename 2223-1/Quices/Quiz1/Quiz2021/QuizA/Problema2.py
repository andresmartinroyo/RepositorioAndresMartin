veterinarians={
    1:{"name":"Luis", "lastName":"Bello","ci":13452224},
    2:{"name":"Jose", "lastName":"Quevedo","ci":44235611},
    3:{"name":"Antonio", "lastName":"Guerra","ci":12345678}
}
mascotas={}
cont=1
while True:
    Zozaya=True
    petdata={}
    print(veterinarians)
    vet=input("Indique su número de veterinario: ")
    if vet.isalpha():
        vet=("Indique su número de veterinario:\n")
    vet=int(vet)
    
    #DNI
    petdata["DNI"]=input("Ingrese el dni del paciente:\n")
    
    while petdata["DNI"].isalpha():
        petdata["DNI"]=input("Ingrese el dni del paciente:\n")
    
    #Nombre PET
    petdata["Nombre de la mascota"]=input("Ingrese el nombre de la mascota:\n")

    while petdata["Nombre de la mascota"].isnumeric():
        petdata["Nombre de la mascota"]=input("Ingrese el nombre de la mascota. ")

    #Chequear si e nombre de la mascota ya fue registrado
    if len(mascotas)>=1:
        for i in range(1,len(mascotas)+1):
            if petdata["Nombre de la mascota"]==mascotas[i]["Nombre de la mascota"] and petdata["DNI"]==mascotas[i]["Nombre de la mascota"]:
                Zozaya=False
    
    #Registrar el resto de datos
    if Zozaya==True:

        #Edad
        petdata["Edad"]=input('Introduce la edad del animal:\n')

        while  petdata["Edad"].isalpha():
            petdata["Edad"]=input('Introduce la edad del animal:\n')

        #Sexo
        petdata["Sexo"]=input('Introduce el sexo del animal. \nM.- Macho. \nH.-Hembra.\n')

        while petdata["Sexo"].isnumeric():
            petdata["Sexo"]=input('Introduce el sexo del animal. \nM.- Macho. \nH.-Hembra.\n')

        #Raza
        petdata["Raza"]=input('Introduce el raza del animal.\n')

        while petdata["Raza"].isnumeric():
            petdata["Raza"]=input('Introduce el raza del animal.\n')

        #Nombre DUENHO
        petdata["Nombre del dueño"]=input('Introduce el nombre del dueño del animal.\n')

        while petdata["Nombre del dueño"].isnumeric():
            petdata["Nombre del dueño"]=input('Introduce el nombre del dueño del animal.\n')

        #Telefono
        petdata["Telefono"]=input('Introduce el telefono del dueño del animal.\n')

        while petdata["Telefono"].isalpha():
            petdata["Telefono"]=input('Introduce el telefono del dueño del animal.\n')

        mascotas[cont]=petdata

        cont=+1
    
    #Factura
    servicio=input("Seleccione cual de los siguientes servicios desea: \n1.-Consulta. \n2.-Operacion \n3.Peluqueria.\n")
    while servicio!="1" and servicio!="2" and servicio and servicio!=3:
        servicio=input("Seleccione cual de los siguientes servicios desea: \n1.-Consulta. \n2.-Operacion \n3.Peluqueria.\n")
    servicio=int(servicio)
    factura=0
    Servicios=[]
    #Coste al cliente
    if servicio == 1:
        factura=20
        Servicios.append("Consulta")
    elif servicio == 2:
        factura=80 
        Servicios.append("Operacion") 
    elif servicio == 3:
        factura=30
        Servicios.append("Peluqueria")
    respuesta=input("Va a desear otra cosa?\nY.-Yes.\nN.-No.\n")
    while respuesta.lower()=="y":
        servicio=input("Seleccione cual de los siguientes servicios desea: \n1.-Consulta. \n2.-Operacion \n3.Peluqueria.\n")
        while servicio!="1" and servicio!="2" and servicio and servicio!=3:
            servicio=input("Seleccione cual de los siguientes servicios desea: \n1.-Consulta. \n2.-Operacion \n3.Peluqueria.\n")
        if servicio == 1:
            factura+=20
            Servicios.append("Consulta")
        elif servicio == 2:
            factura+=80 
            Servicios.append("Operacion") 
        elif servicio == 3:
            factura+=30
            Servicios.append("Peluqueria")
        respuesta=input("Va a desear otra cosa?\nY.-Yes\nN.-No.\n")

    #Imprimir factura

    for key, value in mascotas.items():
        if value["Nombre de la mascota"]==petdata["Nombre de la mascota"] and value["DNI"]==petdata["DNI"]:
            manto=key

    print("El cliente {}, DNI {}, telefono {}; dueño de {}, sexo {}, raza {}, edad {}. Ha realizado una factura de {} por un importe de {}. Ha sido atendido por el vet. {}.".format(mascotas[manto]["Nombre del dueño"], mascotas[manto]["DNI"], mascotas[manto]["Telefono"],  mascotas[manto]["Nombre de la mascota"], mascotas[manto]["Sexo"], mascotas[manto]["Raza"] , mascotas[manto]["Edad"], Servicios, factura, veterinarians[vet]))

    if Zozaya==True:
        cont+=1
            
#Molesete con el ejrecicio
