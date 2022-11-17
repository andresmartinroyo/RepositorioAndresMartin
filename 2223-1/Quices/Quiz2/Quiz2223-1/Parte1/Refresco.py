from Bebidas import Bebidas

class Refresco(Bebidas):
    
    def __init__(self):
        super().__init__()
        self.tipo_de_bebida = "Refresco"
        self.azucar = None
        self.sabor = None

    def agregar_bebidas(self, bebida):
    
        self.nombre =bebida["nombre"]
        self.marca =bebida["marca"]
        self.disponibilidad = bebida["disponible"]
        self.azucar = bebida["azucar"]
        self.sabor = bebida["sabor"]

    def mostrar(self):
        super().mostrar()
        print("El azucar es de: ", self.azucar)
        print("El sabor del refresco es de: ", self.sabor)