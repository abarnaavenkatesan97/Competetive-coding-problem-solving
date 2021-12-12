def revvowels(s):
    myl = []
    st = ""
    for i in range(len(s)):
        if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u" or s[i] == "A" or s[i] == "E" or s[i] == "I" or s[i] == "O" or s[i] == "U":
            myl.append(i)
            st = s[i] + st
    temp = 0
    for i in range(len(myl)):
        s = s[0:myl[i]] + st[temp] + s[myl[i] + 1: ]
        temp = temp + 1
    return s
s = "abcdef"
print(revvowels(s))