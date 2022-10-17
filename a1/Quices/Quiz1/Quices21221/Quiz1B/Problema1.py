num = input("Introduce an integer number: ")
while num.isalpha():
    num = input("Invlaid number. Please enter an iteger number")
num=int(num)
#Validar que num es primo
cont = num-1
if num>=2:
    while num % cont != 0: 
        cont = cont - 1
        if cont == 1:
            aux=1
            break
    if num % cont == 0 and cont != 1 :
        aux=1
    else:
        aux=0
 
#Validar que el output es primo melevaina
if aux==0:
    k=2**num-1
    cont=k-1
    while k % cont != 0: 
        cont = cont - 1
        if cont == 1:
            aux=1
            break
    if num % cont == 0 and cont != 1 :
        aux=1
    else:
        aux=0

if aux==0:
    print(f"El numero {num} es primo melevaina.")