import numpy as np
if __name__ == '__main__':
    N,W,K=map(int,input().split())
    a = list(map(int,input().split()))
    dp=np.full((N+1,W+1),float("inf"))
    dp[0][0]=0
    for i in range(N):
        for w in range(W+1):
            if w-a[i]>=0: # choose
                dp[i+1][w] = min(dp[i+1][w],dp[i][w-a[i]]+1)
            
            dp[i+1][w]=min(dp[i+1][w],dp[i][w]) # not choose 
            
    print("Yes" if dp[N][W]<=K else "NO")


