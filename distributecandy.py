def candycheck(c,n):
    arr = [0] * n
    prev,sums,i = 0,0,0
    while((sums + prev) < c):
        prev += 1
        arr[i] += prev
        sums += prev
        i += 1
        if i == len(arr):
            i = 0
    arr[i] = c - sums
    return arr
if __name__ == "__main__":
    c = int(input())
    n = int(input())
    print(candycheck(c,n))