#Worst case: W(h, m) = h + m - 1
# O(nlog₂n)
def mergesort(n, S):
    h = int(n /2)
    m = n - h
    U = [[0] for i in range(0, h)]
    V = [[0] for i in range(0, m)]

    if(n > 1):
        U[:h] = S[0:h]
        V[:m] = S[h:]
        mergesort(h, U)
        mergesort(m, V)
        merge(h,m,U,V,S)
        
def merge(h, m, U, V, S):
    i = 0
    j = 0
    k = 0
    while(i < h and j < m):
        if(U[i] < V[j]):
            S[k] = U[i]
            i += 1
        else:
            S[k] = V[j]
            j += 1
        k += 1
    if i > h -1 :
        for l in range(j,m):
            S[k] = V[l]
            k+=1
    else :
         for l in range(i,m):
             S[k] = U[l]
             k+=1   

# V를 선언하지 않아도 되므로 공간복잡도 감소  
def mergesort2(low, high, S):
    if(low < high):
        mid = int((low + high)/2)
        mergesort2(low, mid,S)
        mergesort2(mid+1, high,S)
        merge2(low, mid, high, S)

def merge2(low, mid, high, S):
    
    i = low
    j = mid+1
    k = 0
    U = [0]*(high-low +1)
    while(i <= mid and j <= high):
        
        if (S[i] < S[j]):
            U[k] = S[i]
            i += 1
        else:
            U[k] = S[j]
            j += 1
        k += 1

    if (i > mid):
        for l in range(j, high+1):
            U[k] = S[l]
            k += 1
    else:
        for l in range(i, mid+1):
            U[k] = S[l]
            k += 1
            
    for l in range(low, high+1):
        S[l] = U[l-low]
            

    
S = [7,4,3,8,9,14,12,10]
mergesort2(0, 7, S)
print(S)
