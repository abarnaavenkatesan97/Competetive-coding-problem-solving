def duplicates(arr):
    i, l = 0, len(arr) - 1
    myl = []
    inc = 0
    while(i <= l):
        if arr[inc] != 0:
            myl.append(arr[inc])
            i = i + 1
        else:
            myl.append(0)
            myl.append(0)
            i = i + 2
        inc = inc + 1
    if len(myl) > len(arr):
        while(len(myl) > len(arr)):
            myl.remove(myl[-1])
    arr = myl
    return arr
arr = [1,0,0,13,2,0,15,0,0]
print(duplicates(arr))
