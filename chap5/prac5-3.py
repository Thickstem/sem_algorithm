import numpy as np
if __name__ == "__main__":
    N,W = map(int,input().split())
    A = list(map(int,input().split()))
    dp = np.full((N+1,W+1),False)
    dp[0][0]=True
    for i in range(N):
        for w in range(W+1):
            if ~dp[i][w]:
                continue
            dp[i+1][w]=True
            if w+A[i]<W:
                dp[i+1][w+A[i]]=True
    res=0
    for w in range(W+1):
        if dp[N][w]:
            res+=1
    print(res)
    



