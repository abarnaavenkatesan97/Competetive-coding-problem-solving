def counts(s,n):
    i = 0
    m = 0
    while((i + n) <= len(s)):
        temp = s[i:i + n]
        if temp.count("1") > m:
            m = temp.count("1")
        i = i + n
    if i < len(s):
        temp = s[i: ]
        if temp.count("1") > m:
            m = temp.count("1")
    return m
if __name__ == "__main__":
    s = input()
    n = int(input())
    print(counts(s,n))
