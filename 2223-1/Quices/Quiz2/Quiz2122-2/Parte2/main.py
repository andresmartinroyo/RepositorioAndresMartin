from Vehiculos import Vehiculos
from Carros import Carros
from Motos import Motos

def mostrar_vehiculos():

    for vehiculo in Vehiculos.lista_de_vehiculos:

        print("")

        if vehiculo["puesto"] != None:
        
            print("Tipo: ", vehiculo["tipo"])
            print("Placa: ", vehiculo["placa"])
            print("Marca: ", vehiculo["marca"])
            print("Puesto: ", vehiculo["puesto"])
            print("Hora de entrada: ", vehiculo["entrada"])

            if vehiculo is Vehiculos:

                print("Minusvalía: ", vehiculo["minusvalido"])

def main():
    
    print("Bienvenido al sistema.")

    while True:

        respuesta_1 = int(input("Establezca que desea hacer a continuación: \n1.Registrar vehiculo. \n2.Registrar hora de salida.\n3.Ver vehiculos dentro del estacionamiento. \n4. Registrar final del dia.\n==> "))

        if respuesta_1 == 1:

            nuevo_vehiculo_dict={}

            respuesta_2 = int(input("Introduzca el tipo de vehiculo que va a entrar. \n1.Carro.\n2.Moto.\n==>"))

            if respuesta_2 == 1:

                nuevo_vehiculo=Carros()
                nuevo_vehiculo_dict["tipo"]="AUTOMOVIL"
                nuevo_vehiculo.definir_placa()
                nuevo_vehiculo.definir_marca()
                nuevo_vehiculo.definir_puesto()
                nuevo_vehiculo.definir_hora_de_enterada()
                nuevo_vehiculo.estado()

                nuevo_vehiculo_dict["placa"]= nuevo_vehiculo.placa
                nuevo_vehiculo_dict["marca"]= nuevo_vehiculo.marca
                nuevo_vehiculo_dict["puesto"]= nuevo_vehiculo.puesto
                nuevo_vehiculo_dict["entrada"]= nuevo_vehiculo.hora_de_entrada
                nuevo_vehiculo_dict["minusvalido"]= nuevo_vehiculo.estado_de_minusvalia

            elif respuesta_2 == 2:

                nuevo_vehiculo=Motos()
                nuevo_vehiculo.definir_placa()
                nuevo_vehiculo.definir_marca()
                nuevo_vehiculo.definir_puesto()
                nuevo_vehiculo.definir_hora_de_enterada()

                nuevo_vehiculo_dict["tipo"]="MOTOCILETA"
                nuevo_vehiculo_dict["placa"]= nuevo_vehiculo.placa
                nuevo_vehiculo_dict["marca"]= nuevo_vehiculo.marca
                nuevo_vehiculo_dict["puesto"]= nuevo_vehiculo.puesto
                nuevo_vehiculo_dict["entrada"]= nuevo_vehiculo.hora_de_entrada
                
            nuevo_vehiculo_dict["objeto"]=nuevo_vehiculo
            Vehiculos.lista_de_vehiculos.append(nuevo_vehiculo_dict)


        elif respuesta_1 == 2:

                mostrar_vehiculos()

                respuesta_3=input("Introduce la placa del vehiculo que se va a retirar: ")

                for vehiculo in Vehiculos.lista_de_vehiculos:
                    if vehiculo["placa"]==respuesta_3:
                        vehiculo["objeto"].definir_hora_de_salida()
                        vehiculo["salida"] = vehiculo["objeto"].hora_de_salida
                        vehiculo["objeto"].hora_de_salida = None
                        vehiculo["puesto"] = vehiculo["objeto"].hora_de_salida


        elif respuesta_1 == 3: 

            mostrar_vehiculos()

        elif respuesta_1 == 4:

            file = open("Vehiculos_estacionados.txt","a")
            file.write(f"{Vehiculos.lista_de_vehiculos}\n")
            file.close

            Vehiculos.lista_de_vehiculos = []

            print("Se han exportado los datos")

main()

