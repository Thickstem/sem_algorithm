import numpy as np
if __name__ == '__main__':
    N,W=map(int,input().split())
    A=list(map(int,input().split()))
    dp=np.full(W+1,False)
    dp[0]=True
    for w in range(W+1):
        for i in range(N):
            if (dp[w])&(w+A[i]<=W):
                dp[w+A[i]]=True
    print("Yes" if dp[W] else "No")
