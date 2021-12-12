def twosumss(arr,tar):
    myl = []
    res = []
    for i in range(len(arr)):
        if arr[i] not in myl:
            myl.append(tar - arr[i])
        else:
            res.append(myl.index(arr[i]))
            res.append(i)
    return res
            
if __name__ == "__main__":
    tar = int(input())
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input())
    print(twosumss(arr,tar))