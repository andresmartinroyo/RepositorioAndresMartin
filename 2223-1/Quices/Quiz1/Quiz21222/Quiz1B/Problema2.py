pathologies = {
    "Respiratory system": [
        {
            "id": 1,
            "name": "Cystic Fibrosis",
            "price": 300 	
        },
        {
            "id": 2,
            "name": "Emphysema",
            "price": 500
        },
        {
            "id": 3,
            "name": "Tuberculosis",
            "price": 450
        }
    ],
    "Nervous system": [
        {
            "id": 4,
            "name": "Parkinson",
            "price": 800 	
        },
        {
            "id": 5,
            "name": "Epilepsy",
            "price": 600
        }
    ],
    "Endocrine system": [
        {
            "id": 6,
            "name": "Diabetes",
            "price": 350 	
        },
        {
            "id": 7,
            "name": "Acromegaly",
            "price": 700
        },
        {
            "id": 8,
            "name": "Hashimoto’s thyroiditis",
            "price": 900
        }
    ],   
}

pacientes={}
cont=0

while True:

    ans=input("Introduce a continuación la opción que desea realizar. \n1.-Registrar paciente.\n2.-Ver paciente\n==>")
    #Verificar
    while ans.isalpha():
         ans=input("Introduce a continuación la opción que desea realizar. \n1.-Registrar paciente.\n2.-Ver paciente\n==>")

    ans=int(ans)
    if ans==1:
        for sistema,enfermedades in pathologies.items():
            for enfermedad in enfermedades:
                print("\nLa enfermedad {} del {} tiene un id {} y un coste de ${}.".format(enfermedad.get("name"), sistema, enfermedad.get("id"), enfermedad.get("price")))
    
    
        paciente={}
        paciente["nombre"]=input("\nIntroduce el nombre del paciente:\n\n==>")
        #Verificar
        while paciente["nombre"].isnumeric():
            paciente["nombre"]=input("\nIntroduce el nombre del paciente:\n\n==>")

        paciente["apellido"]=input("\nIntroduce el apellido del paciente:\n\n==>")
        #Verificar
        while paciente["apellido"].isnumeric():
            paciente["apellido"]=input("\nIntroduce el apellido del paciente:\n\n==>")


        paciente["DNI"]=input("\nIntroduce el DNI del paciente:\n\n==>")
        #Verificar
        while paciente["DNI"].isalpha():
            paciente["DNI"]=input("\nIntroduce el DNI del paciente:\n\n==>")

        paciente["DNI"]=int(paciente["DNI"])
              
        paciente["id"]=input("\nIntroduce el id de la enfermedad del paciente:\n\n")
        #Verificar
        while paciente["id"].isalpha():
            paciente["id"]=input("\nIntroduce el id de la enfermedad del paciente:\n\n==>")

        paciente["id"]=int(paciente["id"])
        while paciente["id"]<=0 or paciente["id"]>=9:
            paciente["id"]=input("\nIntroduce el id de la enfermedad del paciente:\n\n==>")

        for sistema,enfermedades in pathologies.items():
            for enfermedad in enfermedades:
                if enfermedad["id"]==paciente["id"]:
                    paciente["enfermedad"]=enfermedad["name"]
                    paciente["precio"]=enfermedad["price"]
                    #BONO
                    if str(paciente["DNI"])==str(paciente["DNI"])[::-1]: 
                        print("Paciente apto para descuento.")   
                        paciente["precio"]=enfermedad["price"]*0.7
        
        #Imprimir factura
        print("El paciente {} {} por {}, paga {}".format(paciente.get("nombre"),paciente.get("apellido"), paciente["enfermedad"], paciente.get("precio")))
        pacientes[cont]=paciente
        cont+=1

    elif ans==2:
        for sistema,enfermedades in pathologies.items():
            for enfermedad in enfermedades:
                print("\nLa enfermedad {} del {} tiene un id {}".format(enfermedad.get("name"), sistema, enfermedad.get("id")))
        
        ver=input("\nIntroduce el id de la enfermedad que desea ver los pacientes que la contraen:\n\n==>")
        #Verificar
        while ver.isalpha():
            ver=input("\nIntroduce el id de la enfermedad que desea ver los pacientes que la contraen:\n\n==>")
            
        ver=int(ver)

        for numero, enfermo in pacientes.items():
            if enfermo["id"]==ver:
                print("El paciente {} {}, dni {}. Tiene la enfermedad {}.".format(enfermo["nombre"], enfermo["apellido"], enfermo["DNI"], enfermo["enfermedad"]))

    elif ans==3:
        print("\nEl programa será reiniciado.")
        break

    else:
        pass


