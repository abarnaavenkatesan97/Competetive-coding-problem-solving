def summary(nums):
    myl = []
    if len(nums) == 1:
        myl.append(str(nums[0]))
        return myl
    if len(nums) == 0:
        return myl
    a,b = str(nums[0]),str(nums[0])
    for i in range(1,len(nums)):
        flag = 0
        if nums[i] - 1 != nums[i - 1]:
            flag = 1
        elif nums[i] - 1 == nums[i - 1]:
            b = nums[i]
        if flag == 1:
            if a == b:
                myl.append(str(a))
            else:
                myl.append(str(a) + "->" + str(b))
            a,b = nums[i],nums[i]
    if a == b:
        myl.append(str(a))
    else:
        myl.append(str(a) + "->" + str(b))
    return myl
nums = [0,2,3,4,6,8,9]
print(summary(nums))