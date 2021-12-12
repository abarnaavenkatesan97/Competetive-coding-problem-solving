def palicheck(s):
    i,l = 0,len(s)-1
    times = 0
    ind = None
    while(i < l):
        if (s[i] != s[l]) and (times < 1):
            if s[l] == s[i + 1]:
                ind = i
                i += 1
            elif s[i] == s[l - 1]:
                ind = l
                l = l - 1
            times += 1
        elif (times > 1):
            print(s[i],s[l],i,l)
            return -1
        l -= 1
        i += 1
    if ind == None:
        return -1
    else:
        return ind
if __name__ == "__main__":
    s = input()
    print(palicheck(s))