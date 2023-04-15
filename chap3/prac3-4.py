if __name__ == "__main__":
    inputs = list(map(int,input().split()))
    max,min = -float("inf"),float("inf")
    for num in inputs:
        max = num if num>max else max
        min = num if num<min else min
    
    print(max-min)

