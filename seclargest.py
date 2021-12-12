l = [['Hina', 20], ['Shina', 20.1], ['Tina', 37.2], ['Mina', 20.01], ['Tina', 20.001]]
d = {}
i = 0
j = 1
m = 0
for sub in l:
    for key in sub:
        d[key] = l[i][j]
        i = i + 1
        break

lst = []
for key in d:
    lst.append(d[key])

mi = min(lst)
lst.remove(mi)
m = min(lst)
newlst = []
for key in d:
    if d[key] == m:
        newlst.append(key)
newlst.sort()
for element in newlst:
    print(element)