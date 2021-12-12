def maxi(arr):
    oddsum,evensum = 0,0
    for i in range(0,len(arr),2):
        oddsum = oddsum + arr[i]
    for i in range(1,len(arr),2):
        evensum = evensum + arr[i]
    if oddsum != evensum:
        for i in range(0,len(arr),2):
            while(arr[i] > 0):
                if oddsum == evensum:
                    return sum(arr)
                else:
                    oddsum = oddsum - 1
                    arr[i] = arr[i] - 1
    else:
        return sum(arr)
arr = [5,5]
print(maxi(arr))
