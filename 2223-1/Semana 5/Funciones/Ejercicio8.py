def stats(lista):
    media=sum(lista)/len(lista)
    varianza=0
    for i in lista:
        varianza+=(i-media)**2/len(lista)
    desviacion=varianza**0.5
    return {"Media":media, "Varianza" :varianza, "Desviacion" : desviacion}
print(stats([1,2,3,4,5]))