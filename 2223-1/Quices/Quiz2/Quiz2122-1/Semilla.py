from Productos import Productos
class Semilla(Productos):
    def __init__(self, id, nombre, estock, colores):
        super().__init__(id, nombre, estock, colores)