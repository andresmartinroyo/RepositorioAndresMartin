class Calculadora():
    def __init__(self,numero_de_datos):
        self.numero_de_datos = numero_de_datos
        self.datos=[input(f"Introduce el dato número {indice+1}: ") for indice in range(0,numero_de_datos)]
    
    

class OperacionesBasicas(Calculadora): 

    def __init__(self):
        Calculadora.__init__(self, 2)

    def sumar(self):
        suma=0
        for i in range(self.numero_de_datos):
            suma+=int(self.datos[i])
        return suma
    
    def multiplicacion(self):
        producto=1
        for i in range(self.numero_de_datos):
            producto*=int(self.datos[i])
        return producto

class Raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)

    def raiz_cuadrada(self):
        if self.numero_de_datos==1:
            raiz=float(self.datos[0])**(1/2)
            return raiz
        else:
            print("No se puede calcular raiz de dos terminos, escriba nada mas 1")

def main():
    ejemplo = OperacionesBasicas()

    print(ejemplo.sumar())

    ejemplo2= OperacionesBasicas()

    print(ejemplo2.multiplicacion())

    ejemplo3=Raiz()
    print(ejemplo3.raiz_cuadrada())

main()
