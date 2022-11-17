class Productos:

    lista_productos=[]

    def __init__(self,id,nombre,stock, colores=None):
        self.id = id
        self.nombre = nombre
        self.stock = stock
        self.colores=colores
    
    def mostrar_productos(self):
        print("")
        print("ID: ", self.id)
        print("Nombre: ", self.nombre)
        print("Cantidad en almacen: ", self.stock)
        if self.colores!=None:
            print("Colores: ")
            for color in self.colores:
                print("\t-", color)
        print("")

    def actualizar_stock(self,cantidad_que_le_quiero_quitar):
        self.stock-=cantidad_que_le_quiero_quitar

    