print("============================================\nSucesion de Fibonacci hasta el décimo dígito\n============================================")
a=0
b=1
sum = 0
for i in range (0,50+1):
    print(sum, end=" ")
    a = b
    b = sum
    sum = a + b
