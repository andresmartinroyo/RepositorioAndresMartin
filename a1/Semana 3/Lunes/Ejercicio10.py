sum1 = 0
cont= 0
sum2 = 0
for i in range(6):
    n=int(input("Instert a number: "))
    if n<0:
        sum1=n+sum1
    elif n>0:
        sum2=n+sum2
        cont=cont+1
if cont!=0:
    promedio = sum2/cont
elif cont==0:
    promedio="no fueron introducidos numeros positivos"
print(f"La suma de los numeros negativos es {sum1} y el promedio de los positivos {promedio}.")