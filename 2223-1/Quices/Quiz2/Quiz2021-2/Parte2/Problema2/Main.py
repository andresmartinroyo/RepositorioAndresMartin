
class Recordatorio:
    def __init__(self):
        self.nombre=input("Introduce el nomrbe del recordatorio:")
        self.fecha=input("Introduce la fecha del recordatorio: ")
        self.numero_de_tareas=int(input("Introduce el numero de tareas:"))
    


class Tareas(Recordatorio):
    def __init__(self):
        super().__init__()
        self.tareas=[input(f"Introduce la tarea número {tarea + 1} : ") for tarea in range(self.numero_de_tareas)]
    
    def cambiar_nombre(self,nombre_nuevo):
        self.nombre=nombre_nuevo
    
    def cambiar_fecha(self,fecha_nueva):
        self.fecha=fecha_nueva
    
    def eliminar_tarea(self,tarea_a_eliminar):
        self.tareas=self.tareas.pop(self.tareas[tarea_a_eliminar])

    def agregar_tarea(self):
        self.numero_de_tareas=(self.numero_de_tareas)+1
        self.tareas=self.tareas.append(input("Introduce la tarea que deseas agregar: "))

def main():
    recordatorios_guardados={}
    contar_recordatorios=0

    
    while True:
        
        ans= int(input("\nIntroduce la opcion que deseas realizar:\n1.Crear Recordatorio.\n2.Eliminar recordatorio.\n3.Actualizar recordatorios.\n4.Ver recordatorios.\n5.Desplegar sistema por días.\n==>>"))
        if ans == 1:

            nuevo_recordatorio=Tareas()
            recordatorios_guardados[contar_recordatorios]=nuevo_recordatorio
            contar_recordatorios+=1

        elif ans == 2:
            recordatorio_a_eliminar=input("Introduce el nombre del recordatorio que deseas eliminar: ")
            
            try:
                for n_assignment,assignment in recordatorios_guardados.items():

                    if recordatorios_guardados[n_assignment].nombre==recordatorio_a_eliminar:
                        recordatorios_guardados[n_assignment]=None
                        break
                
                                        
            except:
                print("Ocurrio un error.")

        elif ans == 3:
            recordatorio_a_actualizar=input("Introduce el nombre del recordatorio a actualizar: ")
            try:
                for n_assignment,assignment in recordatorios_guardados.items():
                    if recordatorios_guardados[n_assignment].nombre==recordatorio_a_actualizar:
                        print("\nEl recotdatorio a actualizar ser el siguiente:")
                        print("El recordatorio: ", recordatorios_guardados[n_assignment].nombre)
                        print("Fecha: ", recordatorios_guardados[n_assignment].fecha)
                        print("Tareas: ", recordatorios_guardados[n_assignment].numero_de_tareas)
                        for tarea in assignment.tareas:
                            print("\t-", tarea)
                        
                        respuesta=int(input("Introduce el dato que deseas modificar.\n1.-Nombre.\n2.-Fecha\n3.-Tareas.\n==> "))
                            
                        if respuesta == 1:
                            recordatorios_guardados[n_assignment].cambiar_nombre(input("Introduce el nuevo nombre: "))
                        
                        elif respuesta == 2: 
                            recordatorios_guardados[n_assignment].cambiar_fecha(input("Introduce la nueva fecha."))

                        elif respuesta == 3:
                            respuesta_2=int(input("Indica si desea:\n1.Eliminar un recordatorio.\n2.Agrergar un recordatorio.\n==> "))
                            if respuesta_2==1:
                                recordatorios_guardados[n_assignment].eliminar_tarea(int(input("Introduce el número de tarea que va a eliminar: "))-1)
                            elif respuesta_2==2:
                                recordatorios_guardados[n_assignment].agregar_tareas()
                        else:
                            raise Exception
                        break


                else: 
                    raise Exception
                                    
            except Exception as e:
                print(e)
        
        elif ans == 4:
            for n_assignment,assignment in recordatorios_guardados.items():
                if recordatorios_guardados[n_assignment]!=None:
                    print("\nEl recordatorio: ", recordatorios_guardados[n_assignment].nombre)
                    print("Fecha: ", recordatorios_guardados[n_assignment].fecha)
                    print("Tareas: ", recordatorios_guardados[n_assignment].numero_de_tareas)
                    for tarea in assignment.tareas:
                        print("\t-", tarea)


main()