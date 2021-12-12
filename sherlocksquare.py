def emp(a,b):
    from math import sqrt
    from math import floor
    from math import ceil
    i = ceil(sqrt(a))
    res,c = 0,0
    while res < b:
        res = i * i
        if res > b:
            return c
        c = c + 1
        i = i + 1
    return c    
a = 17
b = 24
print(emp(a,b))