def minimumSwaps(arr): 
    res = 0
    arr = [x-1 for x in arr]
    value_idx = {x:i for i, x in enumerate(arr)}
    for i, x in enumerate(arr):
        if i != x:
            to_swap_idx = value_idx[i]
            print("toswap",to_swap_idx)
            print("i,x",i,x)
            print("arr",arr)
            arr[i], arr[to_swap_idx] = i, x
            value_idx[i] = i
            value_idx[x] = to_swap_idx
            res += 1
    print(res)
    return res
       
arr = [5,1,2,4,3]
print(minimumSwaps(arr))