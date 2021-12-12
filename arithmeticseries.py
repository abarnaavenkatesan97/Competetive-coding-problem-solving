def collectcheck(arr):
    diff = arr[1] - arr[0]
    temp = []
    myl = []
    temp.append(arr[0],arr[1])
    for i in range(2,len(arr)):
        if (arr[i] - arr[i - 1]) == diff:
            temp.append(arr[i])
        else:
            if len(temp) >= 3:
                myl.append(temp)
            temp = []
            temp.append(arr[i - 1])
            temp.append(arr[i])
            diff = arr[i] - arr[i - 1]
    count = 0
    for i in range(len(myl)):
        i = 2
        while(len(myl[i] - i)):
            count = count + len(myl[i]) - i
            i += 1
    return count
if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input())
    print(collectcheck(arr))