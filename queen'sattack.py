def queensAttack(n, k, r_q, c_q, obstacles):
    c = 0
    row,col = r_q,c_q
    while(col < n):
        col = col + 1
        temp = []
        temp.append(row)
        temp.append(col)
        if temp not in obstacles:
            c = c + 1
        else:
            break
    row,col = r_q,c_q
    while(col > 1):
        col = col - 1
        temp = []
        temp.append(row)    
        temp.append(col)
        if temp not in obstacles:
            c = c + 1
        else:
            break
    row,col = r_q,c_q
    while(row < n):
        row = row + 1
        temp = []
        temp.append(row)
        temp.append(col)
        if temp not in obstacles:
            c = c + 1
        else:
            break
    row,col = r_q,c_q
    while(row > 1):
        row = row - 1
        temp = []
        temp.append(row)
        temp.append(col)
        if temp not in obstacles:
            c = c + 1
        else:
            break
    row,col = r_q,c_q
    while(col < n and row > 1):
        row = row - 1
        col = col + 1
        temp = []
        temp.append(row)
        temp.append(col)
        if temp not in obstacles:
            c = c + 1
        else:
            break
    row,col = r_q,c_q
    while(row < n and col > 1):
        row = row + 1
        col = col - 1
        temp = []
        temp.append(row)
        temp.append(col)
        if temp not in obstacles:
            c = c + 1
        else:
            break
    row,col = r_q,c_q
    while(row -1 > 0 and col -1 > 0):
        row = row - 1
        col = col - 1
        temp = []
        temp.append(row)
        temp.append(col)
        if temp not in obstacles:
            c = c + 1
        else:
            break
    row,col = r_q,c_q
    while(row +1 <= n and col +1 <= n):
        row = row + 1
        col = col + 1
        temp = []
        temp.append(row)
        temp.append(col)
        if temp not in obstacles:
            c = c + 1
        else:
            break
    return c
n,k = 100000,0
r_q,c_q = 4187,5068
obstacles = []
print(queensAttack(n,k,r_q,c_q,obstacles))