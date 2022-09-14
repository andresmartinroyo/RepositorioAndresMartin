from operator import ne


savings = float(input("Instert the amount of your deposit; "))
netbenefit1 = savings * 1.04 
netbenefit2 = netbenefit1 * 1.04
netbenefit3 = netbenefit2 * 1.04 
print(f"In the first year youll be having {netbenefit1}, the second year {netbenefit2} and the third year ", round(netbenefit3,2))