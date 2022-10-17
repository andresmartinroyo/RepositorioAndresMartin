infraction={
    1:{"name":"Choque", "cost":50},
    2:{"name":"Semáforo", "cost":30},
    3:{"name":"Falta de documentos", "cost":100},
}

officers={
    1:{"name":"Luis", "lastName":"Bello","ci":13452224},
    2:{"name":"Jose", "lastName":"Quevedo","ci":44235611},
    3:{"name":"Antonio", "lastName":"Guerra","ci":12345678},
}


db={}
cont=0
infractors ={}

while True:
    Zozaya=False #Variable auxiliar que llame asi
    ans=input("What would you like to do?\n1.-Register an infractor.\n2.-Report a payment.\n3.-Show tickets registerded.\n4.-Exit\n==> ")
    while ans.isalpha():
        ans=input("Do not enter alphabetical characters. Enter a valid choice. \n==>")
    ans=int(ans)

    #Diccionario de infractores
    if ans==1 :
        db["Name"]=input("Insert the name of the infractor: ")
        
        #Verificador
        while db["Name"].isnumeric():
            db["Name"]=input("Insert the name of the infractor: ")
        
        db["Last name"]=input("Insert the last name of the infractor: ")
        
        #Verificador
        while db["Last name"].isnumeric():
            db["Last name"]=input("Insert the last name of the infractor: ")
        
        db["ID"]=input("Insert the ID of the infractor: ")
        
        #Verificador
        while db["ID"].isalpha():
            db["ID"]=input("Insert the ID of the infractor: ")

        db["Infraction"]=input("Insert the infraction of the infractor: ")

        #Verificador
        while db["Infraction"].isnumeric(): #¿Cómo iré a meter yo las comparaciones de .lower()!=infracciones y en oficiales
            db["Infraction"]=input("Insert the infraction of the infractor: ")

        db["Officer"]=input("Insert the officers name: ")
        #Verificador
        while db["Officer"].isnumeric():
            db["Officer"]=input("Insert the officers name: ")
        infractors[cont]=db
        cont+=1
    elif ans==2 :
        dni=input("Insert the id of the person that paid.")
        for number,data in infractors.items():
            if dni==infractors[number]["ID"]:
                index=number
                Zozaya=True
        if Zozaya==True:
            infractors.pop(index)
        else:
            print("No se ha encontrado infractor")
    elif ans==3:
        for key, value in infractors.items():
             print("The citizen {} {} of id {} captured by {} commited {} aggression.".format(value["Name"], value["Last name"], value["ID"], value["Officer"], value["Infraction"]), end="\n")
    elif ans==4:
        print("The program will proceed close.")
        break
    else:
        print("Not valid option.")
    
    