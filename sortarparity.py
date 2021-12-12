def sanitycheck(arr,i,myl):
    if len(myl) == 0:
        myl.append(i)
        return arr
    if ((myl[-1] % 2 == 0) and (arr[i] % 2 != 0)) or ((myl[-1] % 2 != 0) and (arr[i] % 2 == 0)):
        arr[myl[-1]],arr[i] = arr[i],arr[myl[-1]]
        myl = myl[ :len(myl)-1]
     
    else:
        myl.append(i)
    return arr
def sotparity(arr):
    myl = []
    for i in range(len(arr)):
        if ((i % 2 == 0) and (arr[i] % 2 != 0)) or ((i % 2 != 0) and (arr[i] % 2 == 0)):
            arr = sanitycheck(arr,i,myl)
            print(arr)
    return arr
if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    print(sotparity(arr))