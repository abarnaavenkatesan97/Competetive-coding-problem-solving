def cavity(grid):
    myl = []
    for i in range(len(grid)):
        myl.append([])
        gri = grid[i]
        for c in gri:
            myl[i].append(c)
    for i in range(len(myl)):
        if i == 0 or i == len(myl) - 1:
            continue
        for j in range(len(myl)):
            if j == 0 or j == len(myl) - 1:
                continue
            if myl[i][j] > myl[i][j - 1] and myl[i][j] > myl[i][j + 1] and myl[i][j] > myl[i - 1][j] and myl[i][j] > myl[i + 1][j]:
                myl[i][j] = "X"
    st = ""
    for i in range(len(grid)):
        st = ""
        for j in range(len(grid)):
            st = st + myl[i][j]
        grid[i] = st
    return grid 
grid = ["1112","1912","1892","1234"]
print(cavity(grid))