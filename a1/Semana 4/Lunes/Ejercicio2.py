A=[[1,2,3],[4,5,6]]
B=[[-1,0],[0,1],[1,1]]
C=[]
acum=0
for i in range(len(A)):
    for j in range(len(A[i])):
        acum+=A[i][j]*B[j][i]
    C.append(acum)

print(C)
