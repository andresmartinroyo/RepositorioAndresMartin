def impuestos(income,IVA=0.21):
    return income*IVA + income

print(impuestos(1000,10))
print(impuestos(1000))