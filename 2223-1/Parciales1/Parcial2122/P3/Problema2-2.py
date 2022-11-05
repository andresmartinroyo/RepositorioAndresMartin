def cliente_mas_adinerado(cuentas):
    max_cuenta=0
    for index in range(len(cuentas)):
        if sum(cuentas[index])>max_cuenta:
            max_cuenta=sum(cuentas[index])
            max_cliente=index
    print(f"El clietne con mas dinero es el numero {max_cliente} con {max_cuenta} uds de dinero")

cliente_mas_adinerado([[1,2,3],[3,2,1]])