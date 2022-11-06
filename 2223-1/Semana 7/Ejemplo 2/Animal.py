class Animal():
    
    def __init__(self, nombre):
        self.nombre= nombre

    def decir_sobre_la_especie(self):
        print("Nombre: ", self.nombre)
        print("Especie: ", self.especie)
        print("Patas: ", self.patas)