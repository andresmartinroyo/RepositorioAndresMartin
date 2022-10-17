n=input("Introduce un número: ")
while n.isalpha() or int(n)<1:
    n=input("Introduce un número: ")
n=int(n)
#primo_de_fermant: n=2**(2**primo)+1


#Buscar los primos menores de n
primos=[2]
for numbers in range(3,n):
    #barrido de numero por numero y detecte si es primo o no. me lo agragee a la lista si lo es
    cont=2
    while cont<=numbers:
        if numbers%cont==0 and numbers!=cont:
            break
        cont+=1
        if numbers==cont:
            primos.append(numbers)
for primo in range(len(primos)):
    test=2**(2**primos[primo])+1
    if test==n:
        print(f"Hermano, el {n} es primo de fermet.")
        break

        
            
