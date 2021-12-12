def cutthestick(arr):
    minarr = []
    minarr = set(arr)
    minarr = list(minarr)
    minarr.sort()
    print(minarr)
    count = len(arr)
    st = ""
    for i in range(len(minarr)):
        if i != 0:
            minarr[i] = minarr[i] - sum(minarr[0:i])  5 - 2  == 2
        count = 0
        for j in range(len(arr)):
            if arr[j] == 0:
                continue
            else:
                arr[j] = arr[j] - minarr[i]
                count = count + 1
        st = st + str(count) + " "
    return st
arr = [5,4,4,2,2,8]
min 2
[3,2,2,0,0,6] 4
[1,0,0,0,0,4] 2


#arr = [66 ,42 ,68 ,72 ,68 ,81 ,91 ,19 ,40 ,73 ,44 ,73 ,89 ,73 ,44 ,12 ,77 ,40 ,44 ,17 ,59 ,99 ,35 ,92 ,80 ,51 ,14 ,30]
print(cutthestick(arr))