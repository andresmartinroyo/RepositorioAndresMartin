from Vehiculos import Vehiculos

class Carros(Vehiculos):
    
    def __init__(self):
        super().__init__()
        self.estado_de_minusvalia = None

    def estado(self):

        if int(input("Es el carro de una persona en condiciones de misvulía?\n1.Sí\n2.No\n==>"))==1:
            self.estado_de_minusvalia = True
        else: 
            self.estado_de_minusvalia = False 


    