n=input("Introduce un numero para verificar que sea par y triangular:  ")

#VErificar naturaleza de la variable n
while n.isalpha():
    n=input("Introduce un numero para verificar que sea par y triangular:  ")
n=int(n)


Zozaya=False
aux=1
var=2

#Verificar su triangularidad
while aux<n:
    aux+=var
    var+=1
    if aux==n:
        Zozaya=True
        break


if Zozaya==True and n%2==0:
    print(f"El numero {n} es par y triangular.")
