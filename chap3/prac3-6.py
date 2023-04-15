if __name__ == "__main__":
    K,N = map(int,input().split())
    num=0
    for i in range(K+1):
        for j in range(K+1):
            z = N-i-j
            if z>=0 and z<=K:
                num+=1
    print(num)

