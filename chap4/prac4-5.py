import numpy as np

if __name__ == "__main__":
    k=int(input("K:"))
    ans=0
    for i in range(100,k):
        tmp_flgs=[0,0,0]
        i_str=str(i)
        for s in i_str:
            if int(s)==3:
                tmp_flgs[0]=1
            elif int(s)==5:
                tmp_flgs[1]=1
            elif int(s)==7:
                tmp_flgs[2]=1
        
        if sum(tmp_flgs)==3:
            ans+=1
    
    print(ans)
                
