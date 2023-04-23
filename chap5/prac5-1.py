import numpy as np
if __name__ == "__main__":
    N = int(input())
    a = np.empty((N,3))
    for n in range(N):
        a[n]= list(map(int,input().split()))
    dp=np.full((N+1,3),0)
    for i in range(N):
        for j in range(3):
            for k in range(3):
                if (j==k):
                    continue
                dp[i+1][k]=max(dp[i+1][k],dp[i][j]+a[i][k])
    
    res = 0
    for i in range(3):
        res = max(res,dp[N][j])
    print(res)

    



        

    
    
