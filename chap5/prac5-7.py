import numpy as np
if __name__ == '__main__':
    S,T = input().split()
    ans = 0
    dp = np.full((S+1,T+1),0)
    dp[0][0]=0
    for i in range(len(S+1)):
        for j in range(len(T+1)):
            if (i>0)&(j>0):
                if S[i-1]==T[j-1]:
                    dp[i][j] = max(dp[i][j],dp[i-1][j-1]+1)
                else:
                    dp[i][j]= max(dp[i][j],dp[i-1][j-1])
            if i>0:
                dp[i][j] = max(dp[i][j],dp[i-1][j])
            if j>0:
                dp[i][j] = max(dp[i][j],dp[i][j-1])
    print(dp[S][T])
