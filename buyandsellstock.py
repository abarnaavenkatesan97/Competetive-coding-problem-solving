def buysellstock(prices):
    if len(prices) == 0:
        return 0
    bp,sp = prices[0],0
    total,profit = 0,0
    for i in range(1,len(prices)):
        if i == len(prices) - 1:
            if prices[i] > sp:
                sp = prices[i]
                total = sp - bp
                if total > profit:
                    profit = total
            continue
        if prices[i] < bp:
            bp = prices[i]
            sp = prices[i + 1]
            total = sp - bp
            if total > profit:
                profit = total
        if prices[i] > sp:
            sp = prices[i]
            total = sp - bp
            if total > profit:
                profit = total
    return profit
prices = [7,6,4,3,1]
print(buysellstock(prices))
