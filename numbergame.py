def myfunc(n):
    temp = n * n
    temp = str(temp)
    n = str(n)
    if int(temp[-1]) == int(n[-1]):
        print("Correct Number")
    else:
        print("Incorrect Number")
    return
if __name__ == "__main__":
    n = int(input())
    if n < 0:
        print("Wrong Input")
    myfunc(n)