def pertenece_a_fibonacci(num):
    n1=0
    n2=1
    for i in range(1,num):
        n1=n1+n2
        n2=n1+n2
        if n1==num or n2==num:
            return True
    return False


def main():
    while True:
        try:
            ans=int(input("Deseas verificar si un número es de la seriue de fibonacci?\n1.-Sí.\n2.-No.\n==>"))
            if ans==1:
                num=int(input("Introduce un número: "))
                if pertenece_a_fibonacci(num):
                    print(f"El número {num} es fibonacci.")
                else :
                    print("No lo es.")
        except:
            print("Hubo un problema. Introducir dato válido.")

main()