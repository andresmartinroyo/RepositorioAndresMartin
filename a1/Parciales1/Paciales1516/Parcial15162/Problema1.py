def ambicioso(num):
    suma=1
    for i in range(2,num):
        if num % i == 0:
            suma+=i
    
    suma2=1
    for i in range(2,suma):
        if suma % i==0:
            suma2+=i
    if suma2==suma:
        return True
    else:
        return False

def main():
    while True:
        try:
            ans=int(input("¿Quieres saber si un número es ambisicioso?\n1.-Sí.\n2.-No.\n==>"))
            if ans == 1:
                num=int(input("Introduce el numero que quieras verificar: "))
                if ambicioso(num):
                    print(f"El numero {num} es ambicioso.")

                else:
                    print(f"El numero {num} NO es ambicioso.")

            elif ans==2:
                break 

        except:
            print("Error")

main()