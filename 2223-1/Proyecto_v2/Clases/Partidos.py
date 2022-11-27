#librerias
import random 

#clases
from Clases.Estadios import Estadios

class Partidos:

    partidos=[]

    def __init__(self):
        self.equipo_local = None
        self.equipo_visitante = None
        self.fecha = None 
        self.hora = None   
        self.id_estadio = None        
        self.id_partido = None       
        self.disponibilidad_de_asientos = None
        self.cantidad_de_asientos = None
        self.codigos_totales = None
        self.codigos_asignados = None
        self.codigos_registrados = None
        self.ventas_total = None
        self.asistencia_total = None

    def definir_partidos(self,diccionario_partidos):
        
        self.equipo_local=diccionario_partidos.get("home_team")
        self.equipo_visitante=diccionario_partidos.get("away_team")
        self.fecha,self.hora=diccionario_partidos.get("date").split(" ")
        self.id_estadio=diccionario_partidos.get("stadium_id")
        self.id_partido=diccionario_partidos.get("id")
        #cortar search aqui
        if diccionario_partidos.get("disponiblidad de asientos") != None:
            self.disponibilidad_de_asientos=diccionario_partidos.get("disponiblidad de asientos")
            self.cantidad_de_asientos=diccionario_partidos.get("canitidad de asientos")
            self.codigos_totales=diccionario_partidos.get("codigos totales")
            self.codigos_asignados=diccionario_partidos.get("codigos asignados")
            self.codigos_registrados=diccionario_partidos.get("codigos registrados")
            if diccionario_partidos.get("ventas total")=="null":
                self.ventas_total=0
            else:
                self.ventas_total=diccionario_partidos.get("ventas total")
            self.asistencia_total=diccionario_partidos.get("asistencia total")

        #Inception para encontrar los asientos disponible
        else:
            self.disponibilidad_de_asientos = []
            for estadio in Estadios.estadios:
                if estadio.id_estadio == self.id_estadio:
                    self.cantidad_de_asientos = estadio.asientos
                    break

            #fila 1 va a ser los numeros del 0 al numero de columnas
            fila=[]
            for columna in range(0, self.cantidad_de_asientos[1]+1):
                fila.append(columna)
            self.disponibilidad_de_asientos.append(fila)

            #Lista de asientos 
            cont = 1
            while cont <=  self.cantidad_de_asientos[0]:
                fila=[]

                #Me esta poniendo espacios en los numeros de manera que si tiene menos de un digito me imprime un espacio para que no se quede cortoen las filas 
                if (cont <= 9):
                    cont = f"{cont} "
                fila.append(cont)
                cont = int(cont)
                cont2=1

                #Me hace lo mismo que arriba, pero con las columans
                while cont2<=self.cantidad_de_asientos[1]:
                    if cont2<10:
                        fila.append("V")
                    else:
                        fila.append(" V")
                    cont2+=1

                cont+=1
                self.disponibilidad_de_asientos.append(fila)
            
                
            lista_de_numeros_unicos = []
            quantity = self.cantidad_de_asientos[0]*self.cantidad_de_asientos[1]
            for i in range(0,quantity):
                Zozaya=False
                while Zozaya==False:
                    x=random.randint(1,2500)
                    if x not in lista_de_numeros_unicos:
                        lista_de_numeros_unicos.append(x)
                        Zozaya=True
            self.codigos_totales=lista_de_numeros_unicos
            self.codigos_asignados = []
            self.codigos_registrados = []
            self.asistencia_total = 0
            
    def mostrar_partido(self):
        print("")
        print("El partido id: ",self.id_partido)
        print("Donde jugará: {} vs {}".format(self.equipo_local,self.equipo_visitante))
        print("A fecha de: ", self.fecha)
        print("A las ", self.hora)
        for estadio in Estadios.estadios: 
            if estadio.id_estadio == self.id_estadio:
                print("En el estadio: ", estadio.nombre)

    #Arreglar esto poara que se vea bonito. Listo
    
    def mostrar_disponibilidad_de_asientos(self,id_partido):
        if self.id_partido==id_partido:
            for fila in self.disponibilidad_de_asientos:
                for valor in fila:
                    print("", valor, end=" ")
                print("")
        
    def contar_ventas(self):
        for partido in Partidos.partidos:
            ventas_del_partido = 0
            for filas in partido.disponibilidad_de_asientos:
                for elemento in filas:
                    if elemento=="O":
                        ventas_del_partido+=1
            partido.ventas_total = ventas_del_partido