def good(p,q):
    from math import sqrt
    f = 0
    for i in range(p,q + 1):
        s1 = i * i
        r = ""
        le = len(str(i))
        while(le):
            temp = s1 % 10
            r = str(temp) + r
            le = le - 1
            s1 = s1 // 10
        l = s1 
        r = int(r)
        if l + r == i:
            f = 1
            print(i,end=" ")
    if f == 0:
        print("INVALID RANGE")
        return
    return
p,q = 1,100
print(good(p,q))
