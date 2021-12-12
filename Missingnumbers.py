def missingNumbers(arr, brr):
    myl = []
    sum1,sum2 = 0,0
    j = 0
    for i in range(len(brr)):
        sum1 = sum1 + brr[i]
        sum2 = sum2 + arr[j]
        if sum1 == sum2:
            pass
        else:
            myl.append(brr[i])
            sum2 = sum2 - arr[j] + brr[i]
            continue
        j = j + 1
        if j == len(arr):
            for k in range(i+1,len(brr)):
                    myl.append(brr[k])
            break
    m = set(myl)
    m1 = list(m)
    m1.sort()
    return m1
arr = [7,2,5,3,5,3,4,5,5,5,5,6,7,11,12]
brr = [7,2,5,4,6,3,5,3]
print(missingNumbers(arr,brr))
