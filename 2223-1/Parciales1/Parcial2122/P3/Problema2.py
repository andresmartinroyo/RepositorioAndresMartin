def main():
    A=[[1,2,3],[4,5,6]]
    B=[[-1,0],[0,1],[1,1]]
    suma=[[0,0],[0,0]]
    for i in range(len(A)):
        for j in range(len(suma)):
            for k in range(len(B)):
                suma[i][j] += A[i][k]*B[k][j]

        
        print(tuple(suma[i]))

main()