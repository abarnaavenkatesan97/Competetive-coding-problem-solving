def relativesort(arr1,arr2):
    
    arr1.sort(key = lambda x : arr2.index(x) if x in arr2 else len(arr2) + x)
    print(arr1)
    return
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(relativesort(arr1,arr2))