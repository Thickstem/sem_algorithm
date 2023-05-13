import numpy as np
from typing import List

def lower_bound(list_:List[int],val:int)->int:
    if val==list_[0]: #左端の扱い方がわからなかったのでゴリ押し
        return 0
    left=0
    right=len(list_)-1
    mid = (right+left)//2

    while(right-left)>1:
        mid = left+(right-left)//2
        if list_[mid]>=val:
            right=mid
        else:
            left=mid    
    return right #idx

if __name__ == "__main__":
    A = list(map(int,input().split()))
    B = np.sort(A) # quick sort. NlogN
    ans=[]
    for i in range(len(A)): # logN
        j = lower_bound(B,A[i])
        ans.append(j)
    print(f"Ans:{ans}")

    
