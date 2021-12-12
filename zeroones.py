def myzerone(arr):
    notevar = None
    for i in range(len(arr)):
        if (notevar == None) and (arr[i] == 0):
            notevar = i-1
            arr[i] = 1
            arr[0] = 0
        elif arr[i] == 0:
            arr[notevar + 1] = 0
            arr[i] = 1
            notevar += 1
    return arr
arr =[1,1,1,1,0,1,0,0,1]
print(myzerone(arr))