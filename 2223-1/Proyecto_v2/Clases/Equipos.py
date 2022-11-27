class Equipos:
    
    equipos=[]

    def __init__(self):
        self.nombre = None
        self.bandera = None
        self.codigo = None
        self.grupo = None
        self.id_equipo = None

    def asignacion_de_datos(self,diccionario_de_equipos):
        self.nombre = diccionario_de_equipos["name"]
        self.bandera = diccionario_de_equipos["flag"]
        self.codigo = diccionario_de_equipos["fifa_code"]
        self.grupo = diccionario_de_equipos["group"]
        self.id = diccionario_de_equipos["id"]

    def mostrar_equipo(self):
        print("")
        print("Equipo: ", self.nombre)
        print("Codigo: ", self.codigo)
        print("Grupo: ", self.grupo)