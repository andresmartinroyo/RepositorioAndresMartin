
def MCD(n1,n2):
    aux1=1
    divisoresn1=[]
    while aux1<=n1:
        if n1%aux1==0:
            divisoresn1.append(aux1)
        aux1+=1
    aux2=1
    divisoresn2=[]
    while aux2<=n2:
        if n2%aux2==0:
            divisoresn2.append(aux2)
        aux2+=1
    divisores_comunes=[]
    for i in divisoresn1:
        for j in divisoresn2:
            if i==j:
                divisores_comunes.append(i)
    return max(divisores_comunes)

def mcm(n1,n2):
    return (n1*n2)/MCD(n1,n2)



print(MCD(24,36))
print(mcm(36,24))