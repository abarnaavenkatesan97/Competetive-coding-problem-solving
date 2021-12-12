def series(n):
    if (n == 1) or (n == 2):
        return 0
    if n % 2 == 0:
        mul = (n - 2) // 2
        mul += 1
        return (7 * mul)
    else:
        mul = (n - 3) // 2
        mul += 1
        return (6 * mul)
if __name__ == "__main__":
    n = int(input())
    print(series(n))