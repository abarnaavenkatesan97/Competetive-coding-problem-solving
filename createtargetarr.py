def createtar(n):
    res=[]
    for i in range(n):
        temp = []
        temp.insert(i,0)
        res.append(temp)
    '''for i in range(len(nums)):
        res.insert(index[i],nums[i])
        print(res)
    '''
    return res
'''nums = [0,1,2,3,4]
index = [0,2,1,2,1]
print(createtar(nums,index))
'''
n = 3
print(createtar(n))