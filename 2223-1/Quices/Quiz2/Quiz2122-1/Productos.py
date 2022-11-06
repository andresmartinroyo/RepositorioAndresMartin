class Productos():

    mercancia= []
    
    def __init__(self, id, nombre, stock, colores):
        self.id = id
        self.nombre = nombre
        self.stock = stock
        self.colores = colores

    def mostrar_productos(self):
        print("\nID: ", self.id)
        print("Nombre: ", self.nombre)
        print("Cantidad en el almacen: ", self.stock)
        if self.colores != None:
            print("Colores: ")
            for color in self.colores:
                print("\t-", color)

    def actualizar_stock(self,amount):
        self.stock-=amount
    
    def buscar_por_id(id):
        for producto in Productos.mercancia:
            if producto.id == id: 
                return producto