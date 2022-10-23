import math

threshold = 1000

# worst case, W(n) = O(n^2)
def prod(u, v):
    if(math.log10(u) > math.log10(v)):
        n = int(math.log10(u)) + 1
    else:
        n = int(math.log10(v)) + 1

    if ( u == 0 or v == 0):
        return 0
    elif (n <= threshold):
        return u * v
    else:
        m = int(n / 2)
        x = u / math.pow(10, m)
        y = u % math.pow(10, m)
        w = v / math.pow(10, m)
        z = v % math.pow(10, m)
        return prod(x,w) * math.pow(10, 2* m) + (prod(x,z) + prod(w, y)) * math.pow(10, m) + prod(y, z)
# worst case, 
def prod2(u, v): W(n) = O(n^1.58)
    if(math.log10(u) > math.log10(v)):
        n = int(math.log10(u)) + 1
    else:
        n = int(math.log10(v)) + 1
        
    if ( u == 0 or v == 0):
        return 0
    elif (n <= threshold):
        return u * v
    else:
        m = int(n/2)
        x = u / math.pow(10, m)
        y = u % math.pow(10, m)
        w = v / math.pow(10, m)
        z = v % math.pow(10, m)
        r = prod2(x + y, w + z)
        p = prod2(x, w)
        q = prod2(y, z)
        return p * math.pow(10, 2*m) + (r-p-q) * math.pow(10, m) + q



u = 326534543
v = 345343453443
print(prod(u,v))
print(prod2(u,v))
