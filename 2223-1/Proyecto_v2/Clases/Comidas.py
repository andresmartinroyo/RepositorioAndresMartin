from Clases.Productos import Productos

class Comidas(Productos):
    def __init__(self):
        super().__init__()
        self.tipo="comida"
        self.coccion = None