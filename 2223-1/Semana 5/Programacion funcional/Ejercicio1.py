def precio_del_inmueble(inmuebles,presupuesto):
    for inmueble in inmuebles:
        if inmueble["zona"]=="A":
            if inmueble["garaje"]:
                precio=(inmueble["metros"]*1000+inmueble["habitaciones"]*5000+15000)*(1-(2022-inmueble["año"])/100)
            else:
                precio=(inmueble["metros"]*1000+inmueble["habitaciones"]*5000)*(1-(2022-inmueble["año"])/100)   
        
        elif inmueble["zona"]=="B":
            if inmueble["garaje"]:
                precio=(inmueble["metros"]*1000+inmueble["habitaciones"]*5000+15000)*(1-(2022-inmueble["año"])/100)*1.5
            else:
                precio=(inmueble["metros"]*1000+inmueble["habitaciones"]*5000)*(1-(2022-inmueble["año"])/100)*1.5
        if precio<=presupuesto:
            print("La vivienda del año {} y cuesta {}.".format(inmueble["año"], precio))
        
def main():
    inmuebles= [    
    {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}   
    ]

    while True:
        presupuesto=int(input("¿Cúal es su presupuesto?\n==>"))
        precio_del_inmueble(inmuebles,presupuesto)
        if input("Di si para salir")=="si":
            break

main()