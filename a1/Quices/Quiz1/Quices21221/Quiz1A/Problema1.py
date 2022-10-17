num = input("Introduce a number: ")

#Verificador de input
while num.isalpha():
    num= input("Not valid, pls enter a number")
    if num.isnumeric():
        break

#Variables definidas para ser usadas en el bucle
amount=len(num)
cont=0
suma=0


for index in range(len(num)):
    #Contador de numeros en str repetidos
    if num[0]==num[index]:
        cont+=1
    suma += int(num[index])


sqrt=suma**0.5
if sqrt==int(sqrt):
    print(f"La suma de los digitos del {num} es {suma} y es cuadrado")

if cont==amount:
    print(f"El número {num} es repunit")