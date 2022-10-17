def primo(ultimo_digito):
    while True:
        try:
            if int(ultimo_digito)==1 or int(ultimo_digito)==2:
                return True
            for i in range(2,int(ultimo_digito)):
                if int(ultimo_digito)%i==0:
                    return False
                return True
        except:
            print("Error 2")

def pedir_nombre():
   nombre_cliente=input("Introduzca el nombre del cliente: ")
   while nombre_cliente.isnumeric():
      nombre_cliente=input("Introduzca el nombre del cliente: ")
   return nombre_cliente

def pedir_cedula():
   descuento=1
   cedula_cliente=input("Introduzca la cedula del cliente: ")
   while cedula_cliente.isalpha():
      cedula_cliente=input("Introduzca la cedula del cliente: ")
   if primo(cedula_cliente[-1]):
      descuento=0.95
   return cedula_cliente, descuento

def pedir_formato_de_pago():
   formatos=["Zelle", "Débito", "Efectivo"]
   while True:
      try:
         formato_cliente=input("Introduzca el formato de pago del cliente. Entre zelle, débito o crédito: ").capitalize().strip()
         print(formato_cliente)
         if formato_cliente not in formatos:
            raise Exception
         return formato_cliente
      except:
         print("Formato invalido")

def mostrar_menu(menu):
    for sabor in menu:
        print("La pizza {} cuenta con los siguientes ingredientes:".format(sabor["pizza"]))
        for ingrediente in sabor["ingredientes"]:
            print(f"\t {ingrediente}")
        print("")
        for coccion, price in sabor["precio"].items():
            print("\t{} tiene un pecio de {}".format(coccion, price.title()))
        print("") 

def pedir_pixa(menu):
    tamaños=["8", "10", "12"]
    sabores_disponibles=["Margarita","Pepperoni","4Estaciones","ProsciuttoFunghi","Española"]
    while True:
        try:

            sabor_de_pizza=input("Introduzca una de las pizzas del menu: ").title()

            if sabor_de_pizza.strip() not in sabores_disponibles:
                raise Exception

            tipo_de_coccion=input("Introduce el tipo de coccion que quieres con tu pizza.\n1.-A la parrila.\n2.-A la leña.\n==>")
            if tipo_de_coccion!="1" and tipo_de_coccion!="2":
                raise Exception
            
            for i in range(0,len(menu)): 
                if sabor_de_pizza==menu[i]["pizza"]:
                    if tipo_de_coccion=="1":
                        subtotal=menu[i]["precio"].get("a la parrilla")
                        break
                    elif tipo_de_coccion=="2":
                        subtotal=menu[i]["precio"]["a la leña"]
                        break
            subtotal=int(subtotal[0:-1])

            tamaño_de_la_pizza=input("Introduce el tamaño de la pizza que deseas: ")

            if tamaño_de_la_pizza not in tamaños:
                raise Exception

            if tamaño_de_la_pizza=="8":
                subtotal=subtotal
            elif tamaño_de_la_pizza=="10":
                subtotal+=5
            elif tamaño_de_la_pizza=="12":
                subtotal+=10
            
            return {"pizza":sabor_de_pizza,"Tamaño":tamaño_de_la_pizza,"Cocción de pizza": tipo_de_coccion,"Subtotal":subtotal}
        except:
            print("Ocurrio un error.")

def delivery_cliente(delivery):
    zonas=["Chacao", "Sucre", "Baruta", "El Hatillo", "Carrizal"]
    while True: 
        try: 
            zona_del_delivery=input("Introduce la zona del delivery: ").title()
            if zona_del_delivery not in zonas:
                raise Exception

            for zona,precio in delivery.items():
                if zona==zona_del_delivery:
                    costo=precio

            return costo, zona_del_delivery
        except:
            print("Hubo un error con la zona que escogió")

def total_a_pagar(cliente,numero_de_pizza_pedida):
    subtotal=0
    for i in range(1,numero_de_pizza_pedida+1):
        subtotal+=cliente[i]["Subtotal"]*cliente["Descuento"]
    total=cliente["delivery"]+subtotal
    return subtotal, total

def maximos_stats(pizza_stats,size_stats,zone_stat):
    maximo_sabor=""
    maxima_pizza=0
    for sabores,q in pizza_stats.items():
        if q>maxima_pizza:
            maximo_sabor=sabores
            maxima_pizza=q
    size_class=""
    size_ammount=0
    for tamaño,cantidad in size_stats.items():
        if cantidad>size_ammount:
            size_class=tamaño
            size_ammount=cantidad
    lugar=""
    lugar_amount=0
    for place,freq in zone_stat.items():
        if freq>lugar_amount:
            lugar_amount=freq
            lugar=place
    
    print(f"El sabor mas pedido {maximo_sabor}.")
        
    print(f"El tamaño mas pedido {size_class}.")
        
    print(f"El muncipio que mas ha pedido {lugar}.")
        
def añadir_a_stats(cliente,pizza_stats,size_stats,zone_stat,numero_de_pizza_pedida):
    if cliente["Zona"] not in zone_stat:
        zone_stat[cliente["Zona"]]=1
    else:
        zone_stat[cliente["Zona"]]+=1
    for i in range(1, numero_de_pizza_pedida+1):
        if cliente[i]["pizza"] not in pizza_stats:
            pizza_stats[cliente[i]["pizza"]]=1
        else :
            pizza_stats[cliente[i]["pizza"]]+=1
        if cliente[i]["Tamaño"] not in size_stats:
            pizza_stats[cliente[i]["Tamaño"]]=1
        else :
            pizza_stats[cliente[i]["Tamaño"]]+=1
    return pizza_stats,size_stats,zone_stat



def main():
    menu = [

   {

      "pizza":"Margarita",

      "ingredientes":[

         "salsa napolitana",

         "queso mozzarella"

      ],

      "precio":{

         "a la parrilla":"6$",

         "a la leña":"8$"

      }

   },

   {

      "pizza":"Pepperoni",

      "ingredientes":[

         "salsa napolitana",

         "queso mozzarella",

         "pepperoni"

      ],

      "tipo":"a la parrilla",

      "precio":{

         "a la parrilla":"8$",

         "a la leña":"10$"

      }

   },

   {

      "pizza":"4 Estaciones",

      "ingredientes":[

         "salsa napolitana",

         "queso mozzarella",

         "jamón",

         "maíz",

         "champiñones",

         "pimentones"

      ],

      "tipo":"a la parrilla",

      "precio":{

         "a la parrilla":"11$",

         "a la leña":"12$"

      }

   },

   {

      "pizza":"Prosciutto Funghi",

      "ingredientes":[

         "salsa napolitana",

         "queso mozzarella",

         "jamón",

         "champiñones",

         "aceite de oliva"

      ],

      "tipo":"a la parrilla",

      "precio":{

         "a la parrilla":"10$",

         "a la leña":"13$"

      }

   },

   {

      "pizza":"Española",

      "ingredientes":[

         "salsa napolitana",

         "queso mozzarella",

         "jamón serrano",

         "salchichón picante"

      ],

      "tipo":"a la parrilla",

      "precio":{

         "a la parrilla":"12$",

         "a la leña":"14$"

      }

   }

]

    delivery = {

   "Chacao":2,

   "Sucre":3,

   "Baruta":4,

   "El Hatillo":4,

   "Carrizal":4

}    

    id_cliente=1
    
    clientes={}

    pizza_stats={}
    size_stats={}
    zone_stat={}

    while True:
        try:
            print("*********Bienvenido***********")
            respuesta=input("Diganos que desea hacer a continuación.\n1.-Pedir pizza.\n2.-Salir.\n3.-Mostrar stats.\n==>")

            while respuesta.isalpha():
                raise Exception
            respuesta=int(respuesta)

            if respuesta==1:
                
                cliente={}
                
                cliente["Nombre"]=pedir_nombre()
                cliente["DNI"],cliente["Descuento"]=pedir_cedula()
                cliente["Formato de Pago"]=pedir_formato_de_pago()
                
                mostrar_menu(menu)

                numero_de_pizza_pedida=1
                
                while True:
                    respuesta_2=input("¿Va a querer continuar con su orden?\n1.-Sí.\n2.-No.\n==>")

                    while respuesta_2.isalpha():
                        respuesta_2=input("¿Va a querer continuar con su orden?\n1.-Sí.\n2.-No.\n==>")
                    respuesta_2=int(respuesta_2)

                    if respuesta_2==1:
                        cliente[numero_de_pizza_pedida]=pedir_pixa(menu)
                    
                    elif respuesta_2==2:
                        cliente["delivery"],cliente["Zona"]=delivery_cliente(delivery)
                        break
                cliente["Sin Delivery"], cliente["Total a pagar"]=total_a_pagar(cliente,numero_de_pizza_pedida)

                print("*******Factura********")
                print("El cliente {}, con cedula {}, ha pedido {} pizzas".format(cliente.get("Nombre"),cliente["DNI"],numero_de_pizza_pedida))
                for i in range(1,numero_de_pizza_pedida+1):
                    print("Una pizza {}, tamaño {} de {}$".format(cliente[i].get("pizza"),cliente[i].get("Tamaño"),cliente[i].get("Subtotal")))
                print("El coste sin delivery es de {}, el costo completo es de {}. Sera pagado en {}".format(cliente["Sin Delivery"], cliente["Total a pagar"],cliente["Formato de Pago"] ))
                clientes[id_cliente]=cliente
                id_cliente+=1
                pizza_stats,size_stats,zone_stat=añadir_a_stats(cliente,pizza_stats,size_stats,zone_stat,numero_de_pizza_pedida)
            elif respuesta==2:
                break
            elif respuesta==3:
                maximos_stats(pizza_stats,size_stats,zone_stat)
            
        except Exception as e:
            print(e)

main()