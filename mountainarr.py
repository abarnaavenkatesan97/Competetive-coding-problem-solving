def lenfinder(i,arr):
    left = i - 1
    right = i + 1
    while((arr[left - 1] < arr[left]) and (arr[right + 1] < arr[right])):
        left -= 1
        right += 1
    return right - left + 1
def mymainfunc(arr):
    if len(arr) <= 2:
        return 0
    myl = []
    for i in range(1,len(arr)-1):
        if (arr[i - 1] < arr[i]) and (arr[i + 1] < arr[i]):
            myl.append(i)
    m = 0
    for i in range(len(myl)):
        temp = lenfinder(myl[i],arr)
        if temp > m:
            m = temp
    return m
if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    print(mymainfunc(arr))