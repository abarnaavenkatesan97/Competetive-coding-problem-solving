def sale(p,d,m,s):
    games = 0
    cost = p
    while(cost <= s):
        if p - d > m:
            cost = cost + (p - d)
            p = p - d
        else:
            cost = cost + m      
        games = games + 1 
        print(cost,p)     
    return games
p = 20
d = 3
m = 6      
s = 106
print(sale(p,d,m,s))