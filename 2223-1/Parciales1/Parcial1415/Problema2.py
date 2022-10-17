def pedir_cedula():
    while True:
        DNI=input("Introduce la cedula del alumno: ")
        if DNI.isnumeric():
            return DNI

def pedir_promedio():
    while True:
        promedio=input("Introduce el promedio del alumno: ")
        if promedio.isnumeric():
            return int(promedio)

def decir_condicion(alumno):
    if alumno["Promedio"] >= 18:
        trimestre="DOS"       
    elif alumno["Promedio"] >= 12 and alumno["Promedio"] < 18:
        trimestre="UNO"
    elif alumno["Promedio"] < 12:
        trimestre="RECHAZADO"

    if trimestre=="RECHAZADO":
        print("El alumno ha sido rechazado.")
    else:
        print(f"El alumno ha sido aceptado en el trimestre {trimestre}.")
    return trimestre

#NO quiere entrar

def contar_alumnos_por_trimestre(alumnos):
    alumnos_1=0
    alumnos_2=0
    alumnos_r=0
    suma_1=0
    suma_2=0
    suma_3=0
    for id,alumno in alumnos.items():
        if alumnos[id]["Condición"]=="UNO":
            alumnos_1+=1
            suma_1=alumnos[id]["Promedio"]
        elif alumnos[id]["Condición"]=="DOS":
            alumnos_2+=1
            suma_2=alumnos[id]["Promedio"]
        elif alumnos[id]["Condición"]=="RECHAZADO":
            alumnos_r+=1
            suma_3=alumnos[id]["Promedio"]

    if alumnos_1!=0:
        promedio_1 = suma_1/alumnos_1
    else: 
        promedio_1=0
    if alumnos_2!=0:
        promedio_2=suma_2/alumnos_2
    else: 
        promedio_2=0
    if alumnos_r!=0:
        promedio_3= suma_3/alumnos_r
    else: 
        promedio_3=0
    SUMA=sum(suma_1, suma_2, suma_3)
    alumnosT=sum(alumnos_1,alumnos_2,alumnos_r)
    promedio_total=SUMA/alumnosT
    print(f"{alumnos_1} van al primer trimestre, {alumnos_2} van al segundo y {alumnos_r} han sido rechazados.")
    print(f"El promedio de los que qudaron el seugndo trimestre fue de {promedio_2}, los que quedaron el primero fue de {promedio_1} y los rechazados fue de {promedio_3}")
    print(f"El promedio general fue de {promedio_total}")

def main():
    alumnos={}
    id_alumno=1

    while True:
        try:
            while True:
                ans=input("¿Qué desea hacer a continuación?\n1.-Registrar estudiante.\n2.-Ver estadísticas.\n==>")
                if ans.isnumeric():
                    break
            if ans == "1":
                alumno={}
                alumno["DNI"]=pedir_cedula()
                alumno["Promedio"]=pedir_promedio()
                alumno["Condición"]=decir_condicion(alumno)
                alumnos[id_alumno]=alumno
                id_alumno+=1
            elif ans=="2":
                print(f"Hay {id_alumno-1} aspirantes.")
                contar_alumnos_por_trimestre(alumnos)
        except:
            print("Error")


main()
