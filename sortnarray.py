def sortarr(arr):
    l = 0
    r = len(arr) // 2
    res = []
    while(r < len(arr)):
        res.append(arr[l])
        res.append(arr[r])
        l += 1
        r += 1
    return res
if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    print(sortarr(arr))