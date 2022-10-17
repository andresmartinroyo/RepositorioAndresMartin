from random import randint


print("\n=================================\nBienvenido a Camarada vs Ondulado\n=================================")
ans=input("¿Qué rol deseas tener?\n1.-Camarada.\n2.-Ondulado.\n")
if ans=="1":
    j1="camarada"
    j2="ondulado"
else:
    j1="ondulado"
    j2="camarada"
print(f"El jugador 1 tendra el rol de {j1} y el jugador 2 {j2}.")


#definidor  de numeros camaradas
sumacamaradas=0
for i in range(3):
    num1=randint(1,9)
    num1=str(num1)
    numt=num1+num1+num1
    numt=int(numt)
    sumacamaradas+=numt
sumaondulados=0
for i in range(3):
    num1=randint(1,9)
    num1=str(num1)
    num2=randint(1,9)
    num2=str(num2)
    numt=num1+num2+num1
    numt=int(numt)
    sumaondulados+=numt
print(f"Ondulados obtiene {sumaondulados} y Camaradas obtiene {sumacamaradas}.")
if sumaondulados>sumacamaradas:
    if ans=="1":
        print("Gana el jugador 2.")
    elif ans== "2":
        print("Gana el jugador 1.")
elif sumacamaradas>sumaondulados:
    if ans=="1":
        print("Gana el jugador 1.")
    elif ans=="2":
        print("Gana el jugador 2")
else:
    print("Empate")
