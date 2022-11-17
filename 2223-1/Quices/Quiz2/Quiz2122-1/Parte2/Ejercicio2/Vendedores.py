from Productos import Productos

class Vendedores:
    todos_mis_clientes=[]
    def __init__(self,cliente,id,cantidad):
        self.cliente = cliente
        self.id = id
        self.cantidad = cantidad
        
    def mostrar(self):
        print("")
        print("Cliente: ", self.cliente)
        print("ID del producto que se lleva: ", self.id)
        print("Cantidad de producto que se lleva: ", self.cantidad)
        print("")
    
    def actualizar_stock(self,cantidad_a_actualizar):
        self.cantidad-=cantidad_a_actualizar

        
"""    #Sergio

    def mostrar(self):
        print(f"productId: {self.productId}")
        print(f"Customer: {self.customer}")
        print(f"Amount: {self.amount}")
        print("")
    
  
    def llenarOrdenado(asc, desc):
        pointerAsc = 0
        pointerDesc = -1

        while (pointerAsc < len(asc)) or (pointerDesc * -1) <= len(desc): #Voy a seguir, hasta haber recorrido las 2 listas
            if (pointerDesc * -1) > len(desc): #Si termine de recorrer el descendente, pero todavia me falta en ascendete
                Vendedores.ordenado.append(Vendedores(asc[pointerAsc][ "product_id"], asc[pointerAsc]["customer_id"], asc[pointerAsc]["amnt"]))
                pointerAsc += 1

            elif pointerAsc == len(asc): #Si termine de recorrer el ascendente, pero todavia me falta en descente
                Vendedores.ordenado.append(Vendedores(desc[pointerDesc][ "product_id"], desc[pointerDesc]["customer_id"], desc[pointerDesc]["amnt"]))
                pointerDesc -= 1
            else:
            
                if asc[pointerAsc]["amnt"] <= desc[pointerDesc]["amnt"]: #Si mi pointer en ascendente es <= a mi pointer en descente  ---> meto el ascendente
                    Vendedores.ordenado.append(Vendedores(asc[pointerAsc][ "product_id"], asc[pointerAsc]["customer_id"], asc[pointerAsc]["amnt"]))
                    pointerAsc += 1
                else:  #Si mi pointer en ascendente es > a mi pointer en descente  ---> meto el descendente
                    Vendedores.ordenado.append(Vendedores(desc[pointerDesc][ "product_id"], desc[pointerDesc]["customer_id"], desc[pointerDesc]["amnt"]))
                    pointerDesc -= 1

        ultimoVendedores = Vendedores.ordenado[-1]
 """
            