def sortarrbyfreq(nums):
    res = []
    d = {}
    for i in range(len(nums)):
        if nums[i] in d:
            d[nums[i]] = d[nums[i]] + 1
        else:
            d[nums[i]] = 1
    while(len(d)):
        m = min(d.values())
        myl = []
        for keys in d:
            if d[keys] == m:
                myl.append(keys)
        myl.sort(reverse=True)
        for i in range(len(myl)):
            while(d[myl[i]]):
                res.append(myl[i])
                d[myl[i]] = d[myl[i]] - 1
            del d[myl[i]]
    return res       
nums = [-1,1,-6,4,5,-6,1,4,1]
print(sortarrbyfreq(nums))
