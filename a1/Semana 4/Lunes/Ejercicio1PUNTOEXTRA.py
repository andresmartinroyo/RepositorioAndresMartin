n=int(input("Enter a number: \n"))
m=int(input("Insert a second number: \n"))
divisores_n=[]
divisores_m=[]
aux=n-1
while aux>0:
    if n%aux==0:
        divisores_n.append(aux)
    aux=aux-1
aux2=m-1
while aux2>0:
    if m%aux2==0:
        divisores_m.append(aux2)
    aux2-=1
    suma1=0
for i in range(len(divisores_n)):
    suma1=suma1+divisores_n[i]
    suma2=0
for i in range(len(divisores_m)):
    suma2=suma2+divisores_m[i]
if suma1==m and suma2==n:
    print("Son numeros amigos.")
