def minimumfind(s,t):
    d = {}
    o = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in t:
        if i in o:
            o[i] += 1
        else:
            o[i] = 1
    count = 0
    for okeys in o:
        found = False
        for dkeys in d:
            if dkeys == okeys:
                found = True
                break
        if (found):
            if o[okeys] <= d[dkeys]:
                pass
            else:
                count = count + (o[okeys] - d[dkeys])
        else:
            count += o[okeys]
    return count
s = "momoqueen"
t = "momeenisg"
print(minimumfind(s,t))
