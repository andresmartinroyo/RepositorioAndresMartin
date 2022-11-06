from Animal import Animal

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.especie = "Canino"
        self.patas = 4
    
perro = Perro("Enrique")
perro.decir_sobre_la_especie()