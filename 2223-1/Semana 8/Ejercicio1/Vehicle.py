class Vehicle:
    def __init__(self,brand,model,color,year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
    def mostrar(self):
        print(f"El vehiculo marca: {self.brand}")
        print(f"El vehiculo moodelo: {self.model}")
        print(f"El vehiculo color: {self.color}")
        print(f"El vehiculo año: {self.year}")
