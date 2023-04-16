class rec:
    def __init__(self) -> None:
        self.counter=0
    def func(self,n,cur,use):
        if cur>n:
            return
        if use==0b111:
            self.counter+=1
        
        self.func(n,cur*10+7,use|0b001)
        self.func(n,cur*10+5,use|0b010)
        self.func(n,cur*10+3,use|0b100)

if __name__ == "__main__":
    n=int(input())
    reccer=rec()
    reccer.func(n,0,0)
    print(reccer.counter)

    