class Bebidas:

    bebidas_bonito= []

    def __init__(self) :

        self.nombre = None
        self.marca = None
        self.disponibilidad = None

    def mostrar(self):  
        
        print("La bebida: ", self.nombre)
        print("De marca: ", self.marca)

        if self.disponibilidad==True:
            print("Esta DISPONIBLE")
        
        elif self.disponibilidad==False:
            print("No esta disponible")



    def cambiar_disponibilidad(self):
        if self.disponibilidad== False:
            print("el producto ay habia sido eliminado.")
        else:
            self.disponibilidad = False

    