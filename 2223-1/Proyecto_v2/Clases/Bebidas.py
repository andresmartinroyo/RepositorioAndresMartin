from Clases.Productos import Productos
class Bebidas(Productos):
    def __init__(self):
        super().__init__()
        self.tipo="bebida"
        self.alcohol =  None
