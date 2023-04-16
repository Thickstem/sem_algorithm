import numpy as np
class trifibo:
    def __init__(self,n):
        self.memo=np.array([-1]*(n+1))
    
    def run(self,n):
        if n==0:
	        return 0
        elif n==1:
            return 0
        elif n==2:
            return 1
        
        if self.memo[n]!=-1:
            return self.memo[n]
        else:
            self.memo[n]=self.run(n-1)+self.run(n-2)+self.run(n-3)
        
        return self.run(n-1)+self.run(n-2)+self.run(n-3)


if __name__ == "__main__":
    n=int(input(f"input n:"))
    fiboner=trifibo(n)
    ret=fiboner.run(n)
    print(ret)
