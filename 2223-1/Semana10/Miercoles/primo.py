def primicidad(numero,divisor):
    if divisor==1:
        return True
    if numero % divisor==0:
        return False
    else:
        return primicidad(numero,divisor-1)

print(primicidad(7,6))