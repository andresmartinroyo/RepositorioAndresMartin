from Articulos import Articulo
import random

class Redactores:
    def __init__(self, nombre, cedula, seccion):
        self.nombre = nombre
        self. cedula = cedula
        self.seccion = seccion
    
    def escribir_articulo(self):
        print("Estoy escribiendo. (tap)(tap)(tap)(tap)")
        articulo = Articulo(
            titulo = input("Titulo: "),
            resumen = input("Resumen: "),
            cuerpo = input("Cuerpo: "),
            fecha_de_redaccion = input("Fecha de reedaccion: "),
            imagenes = input("Imagines: "),
            redactor=self.nombre
            )
        print("\nJeeeefe, te mando el articulo")
        return articulo
    
class Jefe(Redactores):
    def __init__(self, nombre, cedula, seccion):
        super().__init__(nombre, cedula, seccion)

    def supervisar(self):
        print("Todo fino.")
    
    def decidir(self,articulo):
        if random()>0.5:
            print("Se publica el artiuclo {}.".format(articulo.titulo))
            articulo.fecha_de_publicacion="Hoy"
        else:
            print("No se publica el artiuclo {}.".format(articulo.titulo))