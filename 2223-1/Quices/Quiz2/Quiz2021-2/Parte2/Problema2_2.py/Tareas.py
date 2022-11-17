from Recordatorios import Recordatorios

class Tareas(Recordatorios):

    lista_de_recordatrios=[]
    
    def __init__(self):
        super().__init__()
        self.numero_de_tareas = input(int("Introduce el número de tareas que deasea agregar: "))
        self.tareas = [input(f"Indroduce la tarea número {i+1}: ") for i in range(0,self.numero_de_tareas)]

    
    def eliminar_recordatorio(self,lista_de_recordatorios,numero_de_recordatorio_a_eliminar):
        lista_de_recordatorios.pop(numero_de_recordatorio_a_eliminar-1)

    
    