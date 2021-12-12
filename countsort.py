def countsort(arr):
    marr = []
    res = []
    m = max(arr)
    print(m)
    for i in range(m + 1):
        marr.append(0)
    print(len(marr))
    for i in range(len(arr)):
        ind = arr[i]
        marr[ind] = marr[ind] + 1
    for i in range(len(marr)):
        if marr[i] == 0:
            continue
        else:
            while(marr[i]):
                res.append(i)
                marr[i] = marr[i] - 1
    return res
arr = [2,5,9,5,7,6,1,0]
print(countsort(arr))






