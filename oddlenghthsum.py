def oddlensum(arr):
    sums = 0
    if len(arr) % 2 == 0:
        maxoddlen = len(arr) - 1
    else:
        maxoddlen = len(arr)
    while(maxoddlen > 0):
        for i in range(len(arr)):
            temp = i + maxoddlen 
            if temp > len(arr):
                break
            for j in range(i,temp):
                sums = sums + arr[j]
        maxoddlen = maxoddlen - 2   
    return sums
arr = [10,11,12]
print(oddlensum(arr))
        
