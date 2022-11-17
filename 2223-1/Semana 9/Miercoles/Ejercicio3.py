def invertiridor_de_palabras(palabra):
    palabra_nueva=""
    if palabra!="":
        palabra_nueva+=palabra[len(palabra)-1]
        return invertiridor_de_palabras(palabra[0:palabra[len(palabra)-2]])
    if palabra[len(palabra)]==0:
        return palabra_nueva  

def inversor_palabras(palabra, indice):
    if indice==0:
        return palabra[indice]
    return palabra[indice]+inversor_palabras(palabra,indice-1)

def main():
    word=input("Introduce una palbra: ")
    print(inversor_palabras(word,len(word)-1))

main()