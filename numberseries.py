if __name__ == "__main__":
    n = int(input())
    if n == 1 or n == 2:
        print(1)
    if n % 2 == 0:
        t = (n - 4) // 2
        t = t + 1
        print(pow(3,t))
    else:
        t = (n - 3) // 2
        t = t + 1
        print(pow(2,t))