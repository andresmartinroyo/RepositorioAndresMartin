class Vehiculos:
    
    lista_de_vehiculos=[ 
    { "tipo": "AUTOMOVIL", "placa": "ABC12D", "marca": "Chevrolet", "puesto": "A12", "entrada": "10:00:36", "minusvalido": False},
    { "tipo": "AUTOMOVIL", "placa": "IJK56M", "marca": "Mazda", "puesto": "A33", "entrada": "11:48:22", "minusvalido": False},
    { "tipo": "MOTOCICLETA", "placa": "EFG34H", "marca": "Suzuki", "puesto": "B10", "entrada": "10:20:15"}
]

    def __init__(self):
        self.placa = None
        self.marca = None
        self.puesto = None
        self.hora_de_entrada = None
        self.hora_de_salida = None

    def definir_placa(self):
        self.placa=input("Introduce la placa del vehiculo: ")

    def definir_marca(self):
        self.marca = input("Introduce la marca del vehiculo: ")

    def definir_puesto(self):
        self.puesto = input("Introduce el puesto que ocupa el vehiculo: ")

    def definir_hora_de_enterada(self):
        self.hora_de_entrada = input("Introduce la hora de entrada del vehiculo: ")

    def definir_hora_de_salida(self):
        self.hora_de_salida = input("Introduce la hora de salida del vehiculo: ")
        
    def declarar_salida_de_puesto(self):
        self.puesto = None