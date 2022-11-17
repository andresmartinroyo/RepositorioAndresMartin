from Bebidas import Bebidas

class Alcohol(Bebidas):
    
    def __init__(self):
        super().__init__()
        self.tipo_de_bebida = "Alcohol"
        self.grado = None
        self.tipo = None

    def agregar_bebidas(self, bebida):

        self.nombre =bebida["nombre"]
        self.marca =bebida["marca"]
        self.disponibilidad = bebida["disponible"]
        self.grado = bebida["grado"]
        self.tipo = bebida["tipo"]

    def mostrar(self):
        super().mostrar()
        print("El grado es: ", self.grado)
        print("El alcolo es tipo: ", self.tipo)