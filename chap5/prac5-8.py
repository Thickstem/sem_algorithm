import numpy as np
if __name__ == '__main__':
    INF=1<<29
    N,M=map(int,input().split())
    a = list(map(int,input().split()))
    dp = np.full((N+1,M+1),0) # n個の整数までで、m個の区間に分割した時の最適なスコア
    means = np.full((N,N),None)
    for i in range(N): # meanを先に作る。
        for j in range(i):
            means[j][i] = np.mean(a[j:i])
    
    for i in range(N+1):
        for j in range(i):
            for m in range(M):
                dp[i][m]= max(dp[i][m],dp[j][m-1]+means[j][i])


    res = -INF
    for m in range(M):
        res = max(res,dp[N][m])
    print(res)


    