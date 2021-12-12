def triplet(d,arr):
    count = 0
    c = 0
    for i in range(len(arr)):
        t = arr[i]
        c = 1
        for j in range(i,len(arr)):
            if i == j:
                continue
            if c < 3 and arr[j] == t + d:
                t = arr[j]
                c = c + 1
                if c == 3:
                    count = count + 1
                    break
    return count
arr = [2,2,3,4,5]
d = 1
print(triplet(d,arr))
            
