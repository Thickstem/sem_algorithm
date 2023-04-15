if __name__ == "__main__":
    inputs = list(map(int,input().split()))
    trial=0
    flg=1
    while flg:
        for i in range(len(inputs)):
            if inputs[i]%2==0:
                inputs[i]=inputs[i]/2
            else:
                flg=0
                break
        if flg==1:
            trial+=1
    
    print(trial)
    
