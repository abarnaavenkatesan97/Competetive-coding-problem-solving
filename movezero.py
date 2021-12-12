def movezero(nums):
    prev = 2
    idx = 0
    for i in range(len(nums)):
        if (nums[i] == 0) and (prev == 2):
            idx = i
            prev = 0
        elif (nums[i] == 0):
            continue
        else:
            nums[i],nums[idx] = nums[idx],nums[i]
            idx = idx + 1
    return nums
nums = [1,2,0,6,4,3,0]
print(movezero(nums))