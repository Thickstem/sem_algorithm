import numpy as np
if __name__ == "__main__":
    N,W = map(int,input().split())
    A = list(map(int,input().split()))
    dp = np.full((N+1,W+1),False)
    dp[0][0]=True
    for i in range(N):
        for w in range(W+1):
            if dp[i][w]: #A[i]を選ばないとき
                dp[i+1][w]=True
            if (w>=A[i])& dp[i][w-A[i]]:# A[i]を選ぶ時
                dp[i+1][w]=True
    print("Yes" if dp[N][W] else "No")

