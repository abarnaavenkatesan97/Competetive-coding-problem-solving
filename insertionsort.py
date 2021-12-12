def insertionsort(n,arr):
    l = len(arr) - 1
    t = arr[l]
    flag = 0
    for i in range(l - 1,-1,-1):
        print(arr[i],i)
        if flag == 1:
            continue
        elif arr[i] > t:
            arr[i + 1] = arr[i]
            for e in arr:
                print(e,end = " ")
            print(end = "\n")
        else:
            arr[i + 1] = t
            flag = 1
            for e in arr:
                print(e,end = " ")
            print(end = "\n")
    if flag == 0:
        arr[0] = t
        for e in arr:
            print(e,end = " ")
        print(end = "\n")    
            
n = 5
arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
print(insertionsort(n,arr))