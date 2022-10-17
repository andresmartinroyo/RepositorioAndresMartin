def b2d(b):
    b=str(b)[::-1]
    d=0
    for i in range(len(b)):
        if b[i]=="1":
            d+=2**i
    return d

def d2b(decimal):
    binario=""
    while decimal>=1:
        if decimal%2==0:
            binario+="0"
            decimal/=2
        else: 
            binario+="1"
            decimal=(decimal-1)/2
    
    return binario[::-1]

print(b2d(10110))
print(d2b(22))