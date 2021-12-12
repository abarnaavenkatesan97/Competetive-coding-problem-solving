def caesarcipher(s,k):
    st = ""
    print(ord(s))
    if k > 26:
        k = k % 26
    for i in s:
        if (ord(i) in range(65,91)):
            if (k + ord(i)) > ord("Z"):
                s = (k + ord(i)) % ord("Z")
                st = st + chr(s + 65 - 1)
                continue
            st = st + chr(k + ord(i))
        elif (ord(i) in range(97,123)):
            
            if (k + ord(i)) > ord("z"):
                s = (k + ord(i)) % ord("z")
                st = st + chr(s + 97 - 1)
                continue
            st = st + chr(k + ord(i))
            
        else:
            st = st + i
    return st
s = "{"
#s = "DNFjxo?b5h*5<LWbgs6?V5{3M].1hG)pv1VWq4(!][DZ3G)riSJ.CmUj9]7Gzl?VyeJ2dIPEW4GYW*scT8(vhu9wCr]q!7eyaoy."
k = 45
print(caesarcipher(s,k))