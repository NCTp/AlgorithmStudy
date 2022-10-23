def recursive_binarysearch(low, high, S, item):
    if(low > high):
        return 0
    else:
        midPoint = int((low + high) / 2)
        if(item > S[midPoint]):
            return recursive_binarysearch(midPoint+1, high, S, item)
        elif(item < S[midPoint]):
            return recursive_binarysearch(low, midPoint - 1, S, item)
        else:
            return midPoint

S = [1,2,3,4,5,6,7]
print(recursive_binarysearch(0, 6, S, 2))

#Worst case: W(n) = log(n) + 1
#Normal case: log(n)
