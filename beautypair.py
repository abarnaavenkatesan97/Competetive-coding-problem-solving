def beautifulPairs(A, B):
    count = 0
    for i in range(len(B)):
        for j in range(len(A)):
            if A[j] == B[i]:
                A = A[0:j] + A[j+1: ]
                count += 1
                break
    if count == len(B):
        return count - 1
    else:
        count += 1
        return count
A = [1]
B = [1]
print(beautifulPairs(A,B))