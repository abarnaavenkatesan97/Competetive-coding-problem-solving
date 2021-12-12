mylist = [3,2,7,5,1,4]
newlist = []
add = 0
t = 0
c = 0
for i in range(len(mylist)):
    if i == 0:
        pass
    else:
        t = mylist[i]
        mylist[i] = mylist[0]
        mylist[0] = t
    for i in range(1,len(mylist)):
        add = mylist[0] + mylist[i]
        newlist.append(add)
print(newlist)
s = set(newlist)
for element in s:
    if element in mylist:
        c = c + 1
print(c)



        
