import numpy as np
if __name__ == "__main__":
    N,W = map(int,input().split())
    A = list(map(int,input().split()))
    M = list(map(int,input().split()))
    INF = 1<<29
    dp = np.full((N+1,W+1),INF)

    dp[0] = True
    for i in range(N):
        for w in range(W+1):
            # not choose:
            if dp[i][w] < INF:
                dp[i+1][w]  = min(dp[i][w],0)
            # choose
            if (w>=A[i])&(dp[i+1][w-A[i]]<M[i]):
                dp[i+1][w] = min(dp[i+1][w],dp[i+1][w-A[i]]+1)
        

    print("Yes" if dp[N][W]<INF else "No")
