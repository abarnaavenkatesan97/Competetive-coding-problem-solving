def ladybug(b):
    from collections import Counter
    from itertools import groupby
    if '_' in b:
        B = Counter(b)
        print(B)
        del B['_']
        print(B)
        print('NO' if 1 in B.values() else 'YES')
    else:
        # already happy?
        for g in groupby(b):
            print(g,"nuju")
            if len(list(g[1])) == 1:
                print('NO')
                break
        else:
            print('YES')
b = "ACBBC"
print(ladybug(b))