def missingNumbers(arr, brr):
    from collections import Counter
    a = Counter(arr)
    b = Counter(brr)
    return sorted((b - a).keys())
arr = [7,2,5,3,5,3,4,5,5,5,5,6,7,11,12]
brr = [7,2,5,4,6,3,5,3]
print(missingNumbers(arr,brr))