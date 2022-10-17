def cuadrados(muestra):
    resultado=[]
    for i in range(len(muestra)):
        resultado.append(muestra[i]**2)
    return resultado
print(cuadrados([1,2,3,4,5,]))