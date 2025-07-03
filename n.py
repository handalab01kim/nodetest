N=int(input())
A=list(map(int,input().split()))

DP=[0]*N
DP[N-1]=A[N-1]

def 드가자(idx):
    if DP[idx]!=0:
        return DP[idx]

    maxDP=0
    for k in range(idx+1, N):
        if A[k] <= A[idx]: continue
        maxDP = max(maxDP, 드가자(k))
    DP[idx] = A[idx] + maxDP
    print(idx, DP[idx])
    return DP[idx]

print(드가자(0))