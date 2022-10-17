def primidad(numero):
    for i in range(2,numero):
        if numero%i == 0:
            return False
    return True

def main():
    productos={
        "Q":{"name":"Químicos","precio":1000},
        "F":{"name":"Farmacéuticos","precio":2500},
        "B":{"name":"Biológicos","precio":4000}
    }

    comprador_Q=0
    comprador_F=0
    comprador_B=0
    descuento_total_C=0
    descuento_total_R=0
    impuesto_total=0
    max_compra=0
    max_rif=0
    total_total=0

    while True:

        try:

            descuento=0

            #INPUTS
            rif_cliente=input("Introduce el RIF del cliente: ")
            producto_cliente=input("Introduzca la incial del producto que comprará el cliente:\nQ.Químico\nF.Farmacéutico\nB.Biológico.\n==>")
            tipo_de_pago_cliente=input("Introduce el tipo de pago del cliente:\nC.Contado\nR.Crédito\n==>")

            #Precio Bruto
            precio_bruto=productos[producto_cliente]["precio"]

            #Contador de compradores
            if producto_cliente=="Q":
                comprador_Q+=1
            elif producto_cliente=="F":
                comprador_F+=1
            elif producto_cliente=="B":
                comprador_B+=1

            #Descuentos
            if int(rif_cliente[-1]) > 1 and primidad(int(rif_cliente[-1])):
                descuento+=precio_bruto*0.05

            if precio_bruto % 2 == 0:
                descuento += precio_bruto*0.02
            
            if tipo_de_pago_cliente=="C":
                descuento+= precio_bruto*0.03

            impuestos=0
            if producto_cliente!="F":
                impuestos=precio_bruto*0.12
            
            #Contador de descuentos
            if tipo_de_pago_cliente=="C":
                descuento_total_C+=descuento
            elif tipo_de_pago_cliente=="R":
                descuento_total_R+=descuento


            #TOTAL
            total=precio_bruto-descuento+impuestos

            #Total del total
            total_total+=total

            #Máxima compra
            if total>max_compra:
                max_compra=total
                max_rif=rif_cliente

            #Factura
            print("*********Factura**********")
            print(f"RIF: {rif_cliente}")
            print("Producto: {}".format(productos.get(producto_cliente).get("name")))
            print(f"Codigo de pago: {tipo_de_pago_cliente}")
            print(f"SUBTOTAL: {precio_bruto}")
            print(f"DESCUENTOS: {descuento}")
            print(f"IMPUESTOS: {impuestos}")
            print(f"TOTAL: {total}")

            print("")

        except:
            print("Ocurrio un error, vuelva a empezar")

        if input("¿Cerrar caja?\n1.-Si\n2.-No\n==>")=="1":
            break
    print(f"Hubo {comprador_Q} compradores de productos químicos.")
    print(f"Hubo {comprador_F} compradores de productos farmacéuticos.")
    print(f"Hubo {comprador_B} compradores de productos biológicos.")
    print(f"El descuento total fue de los quepagaron al contado fue de {descuento_total_C}.")
    print(f"El descuento total fue de los quepagaron a crédito fue de {descuento_total_R}.")
    print(f"El RIF del máximo comprador fue {max_rif}.")
    print(f"Se facturó un total de {total_total}.")
    

main()