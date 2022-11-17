from Productos import Productos

class Semillas(Productos):
    def __init__(self, id, nombre, stock, colores=None):
        super().__init__(id, nombre, stock, colores)

