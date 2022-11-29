class Productos:
    
    
    def __init__(self, nombre, precio):

        self.nombre= nombre
        self.precio = precio

    def consumir(self):
        print("Estoy consumiendo")

class Bebidas(Productos):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self.tipo="bebida"
        self.alcohol =  None

    def consumir(self):
        print("glup glup glup")
        return super().consumir() 