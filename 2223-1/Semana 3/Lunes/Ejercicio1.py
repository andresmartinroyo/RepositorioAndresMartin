n = int(input("Introduce a positive number. "))
if n%2==0:
    odd= n-1
else:
    odd = n
odds = []
while odd > 0:
    odds.append(odd)
    odd=odd-2
for number in odds:
    print(number, end=", ")
