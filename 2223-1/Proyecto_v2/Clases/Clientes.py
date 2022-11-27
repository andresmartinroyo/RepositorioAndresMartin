#clases
from Clases.Partidos import Partidos
from Clases.Restaurantes import Restaurantes
from Clases.Productos import Productos

#librerias
import itertools
import random

class Clientes:

    clientes = []
    
    def __init__(self):
        self.nombre = None
        self.DNI = None
        self.edad = None
        self.id_partido = None
        self.id_estadio = None
        self.tipo_de_entrada = None
        self.asiento = None
        self.codigo = None
        self.subtotal = None 
        self.descuento = None
        self.iva = None
        self.realizar_pago = None
        self.total = None 
        self.importancia = None
        self.carrito = None
        self.restaurante_del_que_puede_comprar = None
        self.subtotal_restaurante = None
        self.descuento_restaurante = None
        self.iva_restaurante = None
        self.total_restaurante = None
        self.mayoria_de_edad = None
        self.total_total= None

        
    def numero_perfecto(self):
        #Suma de divisores sin incluir al mismo numero igual al numero 6=1+2+3
        suma_divisores=0
        for i in range(1,int(self.DNI)):
            if i % 2 == 0:
                suma_divisores+=i
        if suma_divisores==int(self.DNI):
            return True
        else:
            return False

        
    def numero_vampiro(self):
        #numero vampior tiene un numero 
        # 1.par de digitos,
        # 2. se obtinene al multiplicar dos numeros, llamados colmillos, que tienen la mitada dedigitos que el original
        # 3. Tienen los mismos digitos que los colmillos pero en cualquier orden
        
        #Para la 1
        if len(self.DNI)%2!=0:
            return False

        lista=[]
        for digit in self.DNI:
            lista.append(int(digit))
        r=int((len(lista)/2))
        lista_de_lista_permutaciones=list(itertools.permutations(lista,r))

        permutaciones=[]
        #Los hago string para ooperar mas facil con ellos
        for permutacion in lista_de_lista_permutaciones:
            acum=""
            for digito in permutacion:
                acum+=str(digito)
            permutaciones.append(int(acum))

        #Reviso si las multiplicaciones entre ellos da el DNI
        for permutacion in permutaciones:
            for multiplicador in permutaciones:
                if permutacion*multiplicador==int(self.DNI):
                    return True

        return False

        
    def registrar_cliente(self,id_partido):
        #Datos Personales:
            #Nombre
        while True:
            self.nombre=input("Introduce el nombre del cliente: ")
            if self.nombre.isalpha():
                self.nombre=self.nombre.title()
                break
            #DNI
        while True:
            self.DNI=input("Introduce el numero del documento de identidad del cliente: ")
            if self.DNI.isnumeric():
                break    
            #Edad
        while True:
            self.edad=input("Introduce la edad del cliente: ")
            if self.edad.isnumeric() and int(self.edad)>0:
                break    
        self.edad=int(self.edad)
        
        #Datos de venta
            #El id del partido(que ya pedi en el main)
        self.id_partido=id_partido
            #Tipo de entrada
        while True:
            self.tipo_de_entrada=input("Que tipo de entrada deseas:\n1.General: 50$\n2.VIP: 120$\n==>")
            if self.tipo_de_entrada.isnumeric() and (self.tipo_de_entrada=="1" or self.tipo_de_entrada=="2"):
                break
            
            #Muestro los asientos y pogo el id del estadio al que va

        print("")
        print("V = Vacío")
        print("O = Ocupado")
        print("")
        print("")

        for partido in Partidos.partidos:
            if partido.id_partido==self.id_partido:
                self.id_estadio=partido.id_estadio
                partido.mostrar_disponibilidad_de_asientos(self.id_partido)
            #Asientos
                Martin=False
                while Martin==False:
                        #Aqui estoy pidiendo la columna y revisando que sea escogible 
                    while True:
                        fila = input("Introduce la fila del asiento que deseas comprar: ")
                        if fila.isnumeric() and int(fila)>0 and int(fila)<=partido.cantidad_de_asientos[0]:
                            fila=int(fila)
                            break     
                    
                    while True:
                        columna = input("Introduce la columna del asiento que deseas comprar: ")
                        if columna.isnumeric() and int(columna)>0 and int(columna)<=partido.cantidad_de_asientos[1]:
                            columna=int(columna)
                            break
                        
                    if partido.disponibilidad_de_asientos[fila][columna].replace(" ","")=="V":
                        Martin=True                
                    elif partido.disponibilidad_de_asientos[fila][columna].replace(" ","")=="O":
                        print("El asiento ya estaba ocupado.")
                break
        
            #Estoy poniendo que si la entrada es vip el precio es tanto y si no el precio es otro, aprovechando
            #aprovechando le estoy poniendo los valores correspondientes si el cliente es vip
        if self.tipo_de_entrada=="1":
            self.subtotal = 50
        elif self.tipo_de_entrada =="2":
            self.subtotal = 120
            self.importancia = "VIP"
            self.total_total=self.total
            self.restaurante_del_que_puede_comprar = []
            for restaurante in Restaurantes.restaurantes:
                if restaurante.id_estadio==self.id_estadio:
                    self.restaurante_del_que_puede_comprar.append(restaurante.id_restaurante)
            self.subtotal_restaurante = 0
        
        #Datos de factura
            #Si el clientee tiene dni vampiro, el descuento aplica, si no
        if self.numero_vampiro():
            self.descuento=0.5*self.subtotal
            print("El cliente es váldio para descuento.")
            print("")
        else:
            self.descuento=0

            #Le estoy cobrando IVA por la entrada
        self.iva=self.subtotal*0.16

            #Le estoy preguntando que si quieree continuar con la compra, de ser asi me da un True en 
            #realizar_pago
        while True:
            continuar_compra=input("Desea continuar con el pago?\n1.Si\n2.No\n==>")
            if continuar_compra.isnumeric() and (int(continuar_compra)==1 or int(continuar_compra)==2):
                break
        
        if continuar_compra=="1":
            self.realizar_pago=True
            for partido in Partidos.partidos:
                if partido.id_partido==self.id_partido:
                    partido.disponibilidad_de_asientos[fila][columna].replace("V","O")

        else:
            self.realizar_pago=False

        

            #Si sew me confirma la compra: 1. se añade un total al cliente, 2. se genera un codigo único y aleatorio
            #3. se genera una factura y 4. se ocupa el asiento
        if self.realizar_pago:
            self.total=self.subtotal-self.descuento+self.iva
            self.asiento = [fila,columna]
            for partido in Partidos.partidos:
                if partido.id_partido==self.id_partido:
                    Osorio = False
                    while Osorio == False:
                        codigo_del_cliente=partido.codigos_totales[random.randint(1,len(partido.codigos_totales))]
                        if codigo_del_cliente not in partido.codigos_asignados:
                            partido.codigos_asignados.append(codigo_del_cliente)
                            self.codigo=codigo_del_cliente
                            Osorio = True
            print("")
            print("*********Factura*********")
            print("Cliente: ", self.nombre)
            print("Asiento: ")
            print("\tFila: ", self.asiento[0])
            print("\tAsiento: ", self.asiento[1])
            print("Codigo: ", self.codigo)
            print("Costo:")
            print("\tSubtotal: ", self.subtotal)
            print("\tDescuento: ", self.descuento)
            print("\tIVA: ", self.iva)
            print("\tTotal: ", self.total)
            for partido in Partidos.partidos:
                if partido.id_partido==self.id_partido:
                        partido.disponibilidad_de_asientos[fila][columna]="O"
            print("")
            

                        
    def registrar_compra_restaurante(self):

        #Reviso si el id de estadio del restaurante coincide con le de el estadio del cliente.
        #de ser asi revisa los productos que vende el restaurante coincidiendo sus numeros de restauante
        numero_de_restuarante = 0
        for restaurante in Restaurantes.restaurantes:
            if self.id_estadio == restaurante.id_estadio:
                numero_de_restuarante += 1
                print("")
                print(f"{numero_de_restuarante}. El restaurante, ", restaurante.nombre," tiene:")
                for numero_restaurante , producto in Productos.productos.items():
                    if numero_restaurante == restaurante.id_restaurante:
                        for item in producto:
                            print("")
                            print("\tNombre: ", item.nombre)
                            print("\tPrecio: ", item.precio)
                            print("\tTipo: ", item.tipo)
                            print("")
        
        #Esto es el carrito. Su funcion es que si hay mas de dos reestaurantes por el estadio de un cliente
        #, lo deje escoger, de no ser asi le da por predeterminada una unica opcion. Despues le pide al cliente
        #que meta el nombre de la comida que desea consumir 
        self.carrito={}
        if len(self.restaurante_del_que_puede_comprar) > 1:
            while True:
                print("")
                seleccion_de_restaurante=input("Introduce el restaurante del que deseas comer: ")
                if seleccion_de_restaurante.isnumeric() and (int(seleccion_de_restaurante)>0 and int(seleccion_de_restaurante)<len(self.restaurante_del_que_puede_comprar)):
                    restaurante_del_que_compra=self.restaurante_del_que_puede_comprar[seleccion_de_restaurante-1]
                    break
            
        else:
            restaurante_del_que_compra=self.restaurante_del_que_puede_comprar[0]
        
        while True:
            Zozaya = False 
            while Zozaya == False:    
                cosa=input("Introduce el nombre del producto que quieres: ").title()
                print("")
                if cosa=="Beer" and self.edad<18:
                    print("Tas chiquito, nada de alcohol.")
                    print("")
                    break
                for numero_de_restaurante, producto in Productos.productos.items():
                    if numero_de_restaurante == restaurante_del_que_compra:
                        for item in producto:
                            if item.nombre == cosa and item.cantidad>0:
                                if self.carrito.get(cosa)==None:
                                    self.carrito[cosa]=1
                                else :
                                    self.carrito[cosa]+=1
                                Zozaya=True
                if Zozaya == False:
                    print("Ocurrio un error, vuelva a ingresar el nombre.")
                    print("")

        
            if input("¿Desea continuar con la compra?\n1. Si \n 2. No\n ==> ") == "2" :
                break

        if input("Deseas proceder a pagar o no proceder con la operación?\n1.Pagar\n2.No proceder\n==> ") == "1":
            self.subtotal_restaurante=0
            #Viendo en el carrito los producot sque hay y la cantidad de productos    
            for elemento, cantidad in self.carrito.items():
                for numero_restaurante,producto in Productos.productos.items():
                    for item in producto:
                        if numero_restaurante==restaurante_del_que_compra:
                            if elemento == item.nombre:
                                if self.subtotal_restaurante == 0:
                                    self.subtotal_restaurante = item.precio*cantidad
                                else: 
                                    self.subtotal_restaurante += item.precio*cantidad
                                item.cantidad-=cantidad
            #Esto es para las estadisticas, de esta manera guardo la cantidad de productos que vendo por estadio
            for restaurante in Restaurantes.restaurantes:
                if restaurante_del_que_compra == restaurante.id_restaurante:
                    for elemento, cantidad in self.carrito.items():
                        if restaurante.ventas.get(elemento) == 0:
                            restaurante.ventas[elemento] = cantidad
                        else:    
                            restaurante.ventas[elemento] = cantidad
            
            #Reviso si es apto para descuento
            if self.numero_perfecto():
                self.descuento_restaurante=self.subtotal_restaurante*0.15
            else:
                self.descuento_restaurante=0
            #Le cobro el iva
            self.iva_restaurante=self.subtotal_restaurante*0.16
            #El total_total tambien es para stats, asi veo cuanto gasta cada cliente
            if self.total_total== None:
                self.total_total = 0
            self.total_restaurante=self.subtotal_restaurante-self.descuento_restaurante+self.iva_restaurante
            self.total_total+=self.total_restaurante

            print("")
            print("********FACTURA*******")
            print("El cliente: ", self.nombre)
            print("Costo: ")
            print("\tSubtotal: ", self.subtotal_restaurante)
            print("\tDescuento: ", self.descuento_restaurante)
            print("\tIVA: ", self.iva_restaurante)
            print("\tTotal: ", self.total_restaurante)
            print("")

                     
    def recordar_clientes(self, dict_clientes):
        self.nombre=dict_clientes["nombre"]
        self.DNI=dict_clientes["DNI"]
        self.edad=dict_clientes["edad"]
        self.id_partido=dict_clientes["id_partido"]
        self.id_estadio=dict_clientes["id_estadio"] 
        self.tipo_de_entrada=dict_clientes["tipo_de_entrada"] 
        self.asiento=dict_clientes["asiento"] 
        self.codigo=dict_clientes["codigo"] 
        self.subtotal=dict_clientes["subtotal"]
        self.descuento=dict_clientes["descuento"] 
        self.iva=dict_clientes["iva"] 
        self.realizar_pago=dict_clientes["realizar_pago"] 
        self.total=dict_clientes["total"]
        self.importancia=dict_clientes["importancia"] 
        self.carrito=dict_clientes["carrito"] 
        self.restaurante_del_que_puede_comprar=dict_clientes["restaurante_del_que_puede_comprar"] 
        self.subtotal_restaurante=dict_clientes["subtotal_restaurante"]
        self.descuento_restaurante=dict_clientes["descuento_restaurante"] 
        self.iva_restaurante=dict_clientes["iva_restaurante"] 
        self.total_restaurante=dict_clientes["total_restaurante"]
        self.mayoria_de_edad=dict_clientes["mayoria_de_edad"] 
        self.total_total=dict_clientes["total_total"]

                            



        
                            

                
            