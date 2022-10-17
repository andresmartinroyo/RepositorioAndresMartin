cont=0
numbers = []
while cont < 10 :
    numbers.append(int(input("Enter a number: ")))
    cont = 1 + cont
promedio=0
for i in range(len(numbers)):
    promedio = numbers[i] / len(numbers) + promedio
print(promedio)