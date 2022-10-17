count=0
dic={}
while True:
    ans=int(input(""))
    if ans==1:
        blue=dic[count]={"a":input("a"),"b":input("b"),"c":input("c")}
        count+=1
        print(blue)
    elif ans == 2 :
        print(dic)
    else:
        break