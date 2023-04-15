if __name__ == "__main__":
    string = input()
    n = len(string)
    total_sum=0
    for bit in range(2**(n-1)):
        tmp_idx = []
        tmp_num=0
        for i in range(n-1):
            if bit>>i & 1:
                tmp_idx.append(i)
        if len(tmp_idx)==0:
            total_sum+=int(string)
        else:
            for j in range(len(tmp_idx)):
                if j==0:
                    tmp_num+=int(string[:tmp_idx[j]+1])
                else:
                    tmp_num+=int(string[tmp_idx[j-1]+1:tmp_idx[j]+1])
            tmp_num+=int(string[tmp_idx[j]+1:])
            total_sum+=tmp_num
    
    print(total_sum)
            
            


            
            


