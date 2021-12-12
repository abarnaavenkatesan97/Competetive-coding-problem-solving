def cutTheSticks(arr):
    const = len(arr)
    myl = []
    while(const > 0):
        myl.append(const)
        const = 0
        m = min(arr)
        if m == 0:
            while (m == 0):
                arr.remove(0)
                m = min(arr)
            m = min(arr)
        for i in range(len(arr)):
            if arr[i] == 0:
                continue
            arr[i] = arr[i] - m
            if arr[i] > 0:
                const = const + 1    
    return myl
if __name__ == "__main__":
    n = int(input())
    arr = []
    arr = list(map(int,input().split(" ")))
    myl = []
    myl = cutTheSticks(arr)
    for _ in range(len(myl)):
        print(myl[_])
