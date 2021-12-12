def powerseries(n):
    n -= 1
    if (n == 1) or (n == 2):
        return 1
    if n % 2 == 0:
        mul = (n - 2) // 2
        total = 2
        for i in range(mul):
            total = total * 2
        return total
    else:
        mul = (n - 3) // 2
        total = 3
        for i in range(mul):
            total = total * 3
        return total
if __name__ == "__main__":
    n = int(input())
    print(powerseries(n))