# Worst case : n(n-1)/2
def quicksort(S, low, high):
    if (high > low):
        pivotpoint = partition(S, low, high)
        quicksort(S, low, pivotpoint - 1)
        quicksort(S, pivotpoint + 1 , high)

# T(n) = n-1, 배열의 첫번째 항목을 제외하고 모든 항목을 한번씩 비교하기 때문.
def partition(S, low,  high):
    pivotitem = S[low]
    j = low
    for i in range(low + 1, high + 1):
        if (S[i] < pivotitem):
            j += 1
            S[i], S[j] = S[j], S[i]
            
    S[low], S[j] = S[j], S[low]
    return j





S = [15, 22, 13, 27, 12 ,10, 20 ,25]
quicksort(S,0, 7)
print(S)
