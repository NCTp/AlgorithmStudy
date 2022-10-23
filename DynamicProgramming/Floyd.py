#T(n) = O(n^3)
def floyd(n, W, D):
    D = W
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if (D[i][j] > D[i][k] + D[k][j]):
                    D[i][j] = D[i][k] + D[k][j]
                    
def floyd2(n,W,D):
    for i in range(0, n):
        for j in range(0, n):
            P[i][j] = 0
    D = W
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if (D[i][j] > D[i][k] + D[k][j]):
                    P[i][j] = k
                    D[i][j] = D[i][k] + D[k][j]
            
