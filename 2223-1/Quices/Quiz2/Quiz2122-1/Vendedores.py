from Productos import Productos

class Vendedor:
    ordenado=[]
    
    def __init__(self, id, cliente, cantidad):
        self.id = id
        self. cliente = cliente
        self.cantidad = cantidad
    
    def mostrar_clientes(self):
        print("\nID producto: ", self.id)
        print("Cliente ID: ", self.cliente)
        print("Cantidad que se lleva de producto: ", self.cantidad)

    def actualizar_stock_producto(self):
        
        self.mostrar_clientes()

        producto=Productos.buscar_por_id(self.id)
        producto.actualizar_stock(self.cantidad)

    def ordenar_lista(self,l1,l2):
        indice_l1=0
        indice_l2=-1
        while indice_l1<len(l1) or indice_l2 * -1 <= len(l2):
            if (indice_l2*-1)>len(l2):
                Vendedor.ordenado.append(Vendedor(l1[indice_l1]["product_id"],l1[indice_l1]["costumer_id"],l1[indice_l1]["amnt"]))
                indice_l1+=1

            elif indice_l1== len(l1):
                Vendedor.ordenado.append(Vendedor(l2[indice_l2]["product_id"],l2[indice_l2]["costumer_id"],l2[indice_l2]["amnt"]))
                indice_l2 -= 1

            else: 
                if l1[indice_l1]["amnt"]<=l2[indice_l2["amnt"]]:

                    Vendedor.ordenado.append(Vendedor(l1[indice_l1]["product_id"],l1[indice_l1]["costumer_id"],l1[indice_l1]["amnt"]))
                    indice_l1+=1
                
                else:

                    Vendedor.ordenado.append(Vendedor(l2[indice_l2]["product_id"],l2[indice_l2]["costumer_id"],l2[indice_l2]["amnt"]))
                    indice_l2 -= 1

            ultimovendedor=Vendedor.ordenado[-1]
            ultimovendedor.actualizar_stock_producto()