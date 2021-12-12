def findpalind(s):   
    for j in range(len(s)):
        temp = j
        l = len(s) - 1
        while(temp < l):
            if s[temp] == s[l]:
                checker = s[temp:l + 1]
                if s[temp:l + 1] == checker[ : :-1]:
                    myll = []
                    myll.append(temp)
                    myll.append(l)
                    return myll
            l -= 1
        
def strremoval(s,myl):
    s = s[0:myl[0]] + s[myl[1] + 1: ]
    return s
def mainmyfunc(s):
    c = 0
    while(len(s) > 1):
        myl = []
        myl = findpalind(s)
        afterst = strremoval(s,myl)
        s = afterst
        c += 1
        print(s)
    if len(s) == 1:
        return c + 1
    else:
        return c
s = "bbaabaaa"
print(mainmyfunc(s))