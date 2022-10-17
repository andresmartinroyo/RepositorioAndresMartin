diccionario = {}
while True:
    t = input("Insert an article and its price separated with a space:\n")
    art, price = t.split(" ")
    diccionario[art]=price
    if input("\nDo you want to continue?\nY-Yes\nN-No\n").lower()=="n":
        break
print("\n\nLista de compra", end="\n")
total = 0
for i, j in diccionario.items():
    print(f"{i}\t{j}", end="\n")
    total=total + int(j)
print(f"Total\t{total}")