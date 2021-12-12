def pangram(s):
    st = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    s = s.strip()
    s = set(s)
    c = 0
    for i in s:
        if i in st:
            c = c + 1
    if c >= 26:
        return "pangram"
    else:
        return "not pangram"
s = "We promptly judged antique ivory buckles for the next prize"
print(pangram(s))