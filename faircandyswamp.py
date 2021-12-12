def fairswap(A,B):
    myl = []
    eq = (sum(A) + sum(B)) // 2
    if sum(B) > sum(A):
        const = sum(B) - eq
        for i in range(len(B)):
            if (B[i] - const) in A:
                myl.append(B[i] - const)
                myl.append(B[i])
                return myl
    elif sum(B) < sum(A):
        const = sum(A) - eq
        for i in range(len(A)):
            if (A[i] - const) in B:
                myl.append(A[i])
                myl.append(A[i] - const)
                return myl
    else:
        myl.append(min(A))
        myl.append(min(B))
        return myl
A = [1,2,5]
B = [2,4]
print(fairswap(A,B))