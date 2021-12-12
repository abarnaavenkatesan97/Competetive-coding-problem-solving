def myarrrev(arr):
    first = 0
    last = len(arr) - 1
    while(first <  last):
        arr[last],arr[first] = arr[first],arr[last]
        first += 1
        last -= 1
    return arr
arr = [0,2,4,6,8,10]
print(myarrrev(arr))