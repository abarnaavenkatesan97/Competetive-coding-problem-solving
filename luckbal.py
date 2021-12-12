def luckBalance(k, c):
    zerosum = 0
    myl = []
    for i in range(len(c)):
        if c[i][1] == 0:
            zerosum += c[i][0]
        else:
            myl.append(c[i][0])
    if len(myl) == 0:
        return zerosum
    myl.sort(reverse = True)
    onesum = 0
    i = 0
    while(i < k and i < len(myl)):
        onesum += myl[i]
        i += 1
    onesum = onesum - sum(myl[i:len(myl)])
    return onesum + zerosum
k = 4
c = [[5,0],[4,1],[2,1]]
print(luckBalance(k,c))