def duplicatezeroes(arr):
    i = 0
    nex = []
    while(i <= len(arr)-1):
        if (len(nex) == 0) and (arr[i] != 0):
            i += 1
            continue
        elif (len(nex) == 0) and (arr[i] == 0):
            nex.append(arr[i + 1])
            arr[i + 1] = 0
            i += 2
            continue
        if (len(nex) != 0) and (nex[0] != 0):
            temp = arr[i]
            arr[i] = nex[0]
            nex.append(temp)
            i += 1
            nex = nex[1: ]
        elif (len(nex) != 0) and (nex[0] == 0):
            try:
                temp = arr[i]
                nex.append(temp)
                arr[i] = 0
            except:
                pass
            try:
                temp = arr[i + 1]
                nex.append(temp)
                arr[i + 1] = 0
            except:
                pass
            i += 2
            nex = nex[1: ]
    return arr
arr = [0,3,0,8,2,0,8]
print(duplicatezeroes(arr))





