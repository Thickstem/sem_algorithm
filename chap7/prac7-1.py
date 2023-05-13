import numpy as np

def pair_search(A,B):
    for i in range(len(B)):
        for j in range(len(A)):
            if B[i]<=A[j]:
                ans+=1
                A = A[j:]
                if len(A)==1:
                    return ans
                else:
                    continue

if __name__ == "__main__":
    A = np.sort(np.array(map(int,input().split()))) # quick sort NlogN
    B = np.sort(np.array(map(int,input().split()))) # quick sort NlogN
    N = len(A)
    ans = pair_search(A,B)
    print(f"ans:{ans}")
    



