from Flores import Flores
from Productos import Productos
from Semillas import Semillas
from Vendedores import Vendedores

def mostrar():
    for elementos in Productos.lista_productos:
        Productos.mostrar_productos(elementos)

def mostrar_lista(clientes_ordenados):
    for clientes in clientes_ordenados:
        clientes.mostrar()

"""def ordernarVendedores(asc, desc):
    Vendedores.llenarOrdenado(asc, desc)"""


def ordenar_clientes(clientes_desordenados):
    clientes=clientes_desordenados
    clientes_ordenados=[]

    
    while True:
        min=clientes[0].cantidad 
        indice=0   
        for cliente in range(len(clientes)):
            if clientes[cliente].cantidad<min:
                min=clientes[cliente].cantidad
                indice=cliente
        clientes_ordenados.append(clientes[indice])
        clientes.pop(indice)
        if len(clientes)<1:
            return clientes_ordenados


def main():
    products = [
{ "id": 1, "name": "Rose", "type": "flower", "stock": 160, "colors": ["red", "white", "pink"] },
{ "id": 2, "name": "Tulip", "type": "flower", "stock": 34, "colors": ["white", "yellow"] },
{ "id": 3, "name": "Sunflower seeds", "type": "seeds", "stock": 50 },
{ "id": 4, "name": "Sunflower", "type": "flower", "stock": 77, "colors": ["yellow"] },
{ "id": 5, "name": "Lavender seeds", "type": "seeds", "stock": 100, "colors": ["purple"] },
{ "id": 6, "name": "Carnation", "type": "flower", "stock": 89, "colors": ["yellow", "burgundy", "purple", "pink", "red", "white"] },
]
    
    vendor_1 = [
{ "product_id": 5, "customer_id": 333, "amnt": 1 },
{ "product_id": 5, "customer_id": 1010, "amnt": 2 },
{ "product_id": 3, "customer_id": 1111, "amnt": 3 },
{ "product_id": 2, "customer_id": 222, "amnt": 6 },
{ "product_id": 6, "customer_id": 444, "amnt": 7 },
{ "product_id": 1, "customer_id": 1111, "amnt": 20 }
]
 
    vendor_2 = [
{ "product_id": 6, "customer_id": 888, "amnt": 10 },
{ "product_id": 1, "customer_id": 123, "amnt": 5 },
{ "product_id": 2, "customer_id": 321, "amnt": 4 },
{ "product_id": 4, "customer_id": 555, "amnt": 2 },
{ "product_id": 1, "customer_id": 777, "amnt": 1 }
]
    
    while True:
        

        ans=int(input("Introduce una opcion.\n1.-Ver Inventario.\n2.-Actualizar inventario y ver clientes:\n==> "))
        
        if ans == 1:
            for producto in products:
                if producto["type"]=="flower":
                    
                    Productos.lista_productos.append(Flores(producto["id"],producto["name"],producto["stock"],producto.get("colors")))

                elif producto["type"]=="seeds":
                    
                    Productos.lista_productos.append(Semillas(producto["id"],producto["name"],producto["stock"],producto.get("colors")))
            mostrar()

        elif ans==2:
            
            
            
            for vendedor in vendor_1:
                Vendedores.todos_mis_clientes.append(Vendedores(vendedor["customer_id"],vendedor["product_id"],vendedor["amnt"]))
                
            for vendedor in vendor_2:
                Vendedores.todos_mis_clientes.append(Vendedores(vendedor["customer_id"],vendedor["product_id"],vendedor["amnt"]))

            clientes_ordenados=ordenar_clientes(Vendedores.todos_mis_clientes)
            mostrar_lista(clientes_ordenados)


            for venta in clientes_ordenados:
                id_producto=venta.id
                cantidad_de_producto=venta.cantidad
                for product in Productos.lista_productos:
                    if product.id==id_producto:
                        product.actualizar_stock(cantidad_de_producto)
            
            mostrar()

        
        
        else:
            break




main()