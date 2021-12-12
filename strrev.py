def mystrrev(s):
    first = 0
    last = len(s) - 1
    while(first < last):
        s = s[0:first] + s[last] + s[first+1:last] + s[first] + s[last+1: ]
        first += 1
        last -= 1
    return s
s = "apisero"
print(mystrrev(s))
