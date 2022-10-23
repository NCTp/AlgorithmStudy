# O(n^3)
def matrixmult(n, A, B , C):
    for i in range(0, n):
        for j in range(0, n):
            #C[i][j] = 0
            for k in range(0, n):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
                print(C[i][j])
A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
C = [[0,0],[0,0]]
matrixmult(2,A,B,C)
print(C)
        
