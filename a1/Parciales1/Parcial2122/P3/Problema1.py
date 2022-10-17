def main():
    while True:
        ans=input("Introduce el codigo que quieres traducir: ")
        traduccion=ans.replace("G","g").replace("()","o").replace("(al)","al")
        print(traduccion)
        pregunta=input("Quieres salir?\nY.Yes\nN.No\n=>").upper()
        if pregunta=="Y":
            break

main()