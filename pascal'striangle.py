def pascaltriangle(numrows):
    myl = []
    for i in range(1,numrows + 1):
        temp = []
        j = i
        while(j):
            temp.append(1)
            j = j - 1
        myl.append(temp)
    print(myl)
    for i in range(len(myl)):
        for j in range(len(myl[i])):
            if (j == 0) or (j == len(myl[i]) - 1):
                continue
            else:
                myl[i][j] = myl[i - 1][j] + myl[i - 1][j - 1]
    return myl
numrows = 6
print(pascaltriangle(numrows))