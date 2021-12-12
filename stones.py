def stones(n,a,b):
    first_term=(n-1)*min(a,b)
    difference=max(a,b)-min(a,b)
    myl = []
    myl.append(first_term)
    if(difference>0):
        for j in range(n-1):
            first_term+=difference
            myl.append(first_term)
            
    return myl
n = 3
a = 1
b = 2
print(stones(n,a,b))