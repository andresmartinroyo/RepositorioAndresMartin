class Articulo:
    def __init__(self, titulo, resumen, cuerpo, fecha_de_redaccion,redactor,imagenes, fecha_de_publicacion=None,):
        self.titulo = titulo
        self.resumen = resumen
        self.cuerpo = cuerpo
        self.fecha_de_redaccion = fecha_de_redaccion
        self.imagenes = imagenes
        self.fecha_de_publicacion = fecha_de_publicacion
        self.redactor = redactor
