from Clases.Restaurantes import Restaurantes
from Clases.Productos import Productos
from Clases.Bebidas import Bebidas
from Clases.Comidas import Comidas

class Estadios():

    estadios=[] 

    def __init__(self):
        self.id_estadio = None
        self.nombre = None
        self.capacidad = None
        self.asientos = None
        self.localizacion = None
        self.restaurantes = None

    #Para no recorerrer el json en cada calse, lo voy a hacer solo en esta
    def definir_estadios_restaurantes_productos(self,diccionario_de_estadios):

        #Aqui estoy pidiendo los datos del API, para el estadio

        self.id_estadio = diccionario_de_estadios.get("id")
        self.nombre = diccionario_de_estadios.get("name")
        self.asientos = diccionario_de_estadios.get("capacity")
        self.capacidad = diccionario_de_estadios.get("capacity")[0]*diccionario_de_estadios.get("capacity")[1]
        self.localizacion = diccionario_de_estadios.get("location")
        
        #Me voy a poner a ver en el o los restaurante(s) de cada estadio y ponerle un id al restuarante para que asi pueda pasarle los productos que tiene 
        
        id_del_restaurante=len(Restaurantes.restaurantes)+1
        for restaurant in diccionario_de_estadios.get("restaurants"):

            lugar=Restaurantes()

            #hacer lugar.nombre, lugar.id_estadio, etc. Despues hacer otro for para 

            lugar.nombre = restaurant.get("name")
            lugar.id_estadio = self.id_estadio
            lugar.id_restaurante = id_del_restaurante
            #Ver los productos de la API por restaurante
            lista_de_productos=[]
            productos_vendidos={}
            for producto in restaurant.get("products"):
                if producto["type"]=="beverages":
                    cosa = Bebidas()
                    if producto["adicional"]=="alcoholic":
                        cosa.alcohol = True
                    else:
                        cosa.alcohol=False
                if producto["type"]=="food":
                    cosa = Comidas()
                    if producto["adicional"]=="plate":
                        cosa.coccion = True
                    else:
                        cosa.coccion=False
                cosa.nombre=producto["name"].title()
                cosa.cantidad = producto["quantity"]
                cosa.precio=producto["price"]
                lista_de_productos.append(cosa)
                productos_vendidos[cosa.nombre]=25-cosa.cantidad 
            lugar.ventas=productos_vendidos               
            Productos.productos[lugar.id_restaurante]=lista_de_productos
            id_del_restaurante+=1
            Restaurantes.restaurantes.append(lugar)
            lugar.id_estadio = diccionario_de_estadios.get("id")




        

        


    def mostrar_estadio(self):
        
            print("")
            print("El estadio: ", self.nombre)
            print("Con id: ", self.id_estadio)
            print("Tiene una capacidad de: ", self.capacidad)
            print("Esta en: ", self.localizacion)
            print("Tiene los siguientes restaurantes, donde venden:")
            for restaurante in Restaurantes.restaurantes:
                print("")
                print("\t- ", restaurante.nombre)
                for id_restaurante, productos in Productos.productos.items():
                    if id_restaurante==restaurante.id_restaurante:
                        for producto in productos:
                            print("")
                            print("\t\t-Nombre: ", producto.nombre)
                            print("\t\t-Precio: ", producto.precio)
                            if producto.cantidad!=0:
                                print("\t\t-Tipo: ", producto.tipo)
                            print("")
                print("")
            print("")


