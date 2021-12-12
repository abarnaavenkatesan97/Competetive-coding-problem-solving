def chessboard(board):
    p = []
    b = []
    r = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == "p":
                t = []
                t.append(i)
                t.append(j)
                p.append(t)
            elif board[i][j] == "B":
                t = []
                t.append(i)
                t.append(j)
                b.append(t)
            elif board[i][j] == "R":
                t = []
                t.append(i)
                t.append(j)
                r.append(t)
    print(r)
    print(b)
    print(p)
board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
print(chessboard(board))
