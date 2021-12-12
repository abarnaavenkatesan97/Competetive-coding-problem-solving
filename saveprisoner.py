def saveThePrisoner(n, s, pos):
    if n > s:
        pos = pos - 1
        res = pos + s
        if res > n:
            if res % n == 0:
                res = n
                return res
            else:
                res = res % n
                return res
        else:
            return res
    else:
        res = pos + s - 1
        if res > n:
            if res % n == 0:
                res = n
                return res
            else:
                res = res % n
                return res
        else:
            return res
n = 5
s = 2
pos = 2
print(saveThePrisoner(n,s,pos))