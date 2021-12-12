def counttriplet(arr,a,b,c):
    count = 0
    for i in range(len(arr) - 2):
        for j in range(i + 1,len(arr)):
            for k in range(j + 1,len(arr)):
                print(i,j,k)
                if abs(arr[i] - arr[j]) <= a:
                    if abs(arr[j] - arr[k]) <= b:
                        if abs(arr[i] - arr[k]) <= c:
                            count = count + 1
    return count
arr = [1,1,2,2,3]
a = 0
b = 0
c = 1
print(counttriplet(arr,a,b,c))