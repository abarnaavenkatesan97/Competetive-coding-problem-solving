def checkequality(myl,n):
    half = n // 2
    half -= 1
    for i in range(len(myl)):
        sums1,sums2 = 0,0
        for j in range(len(myl[0])):
            if (myl[i][j] == "0") or ((n % 2 != 0) and (j == half + 1)):
                continue
            if j <= half:
                sums1 += 1
            else:
                sums2 += 1
        if (sums1 == sums2) and (myl[i][0] != "0"):
            print(myl[i],end=" ")
def printmyl(myl):
    for i in range(len(myl)):
        for j in range(len(myl[0])):
            print(myl[i][j],end=" ")
        print()
                
def printbinary(n):
    mul = 1
    times = n
    while(times):
        mul *= 2
        times -= 1
    limit = mul // 2
    zeroflag = True
    temp = 1
    myl = []
    for i in range(n):
        for j in range(mul):    
            if i == 0:
                myl.append("")
            if zeroflag:
                myl[j] += "0"
            else:
                myl[j] += "1"
            temp += 1
            if temp > limit:
                if zeroflag:
                    zeroflag = False
                else:
                    zeroflag = True
                temp = 1
        limit = limit // 2
    return myl
n = 4
myl = printbinary(n)
printmyl(myl)
checkequality(myl,n)

        
