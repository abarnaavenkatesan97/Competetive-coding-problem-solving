
def checker(row,col,myl,elem):
    c = 0
    for i in range(3):
        if myl[row][i] == elem:
            c = c + 1
    if c == 3:
        return True
    c = 0
    for i in range(3):
        if myl[i][col] == elem:
            c = c + 1
    if c == 3:
        return True
    c = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                if myl[i][j] == elem:
                    c = c + 1
    if c == 3:
        return True
    c = 0
    temp = 0
    for i in range(2,-1,-1):
        if myl[temp][i] == elem:
            c = c + 1
        temp = temp + 1
    if c == 3:
        return True
    return False    
def tictactoe(moves):
    myl = []
    for i in range(3):
        myl.append([])
        myl[i].append(" ")
        myl[i].append(" ")
        myl[i].append(" ")
    for i in range(len(moves)):
        row = moves[i][0]
        col = moves[i][1]
        if i % 2 == 0:
            myl[row][col] = "X"
            elem = "X"
            if checker(row,col,myl,elem):
                return "A"
        else:
            myl[row][col] = "O"
            elem = "O"
            if checker(row,col,myl,elem):
                return "B"
    if len(moves) < 9:
        return "Pending"
    return "Draw"
moves = [[0,0],[1,1]]
print(tictactoe(moves))