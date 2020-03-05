def max_distinct(S,n):
    c = [0]*256
    for i in range(n):
        c[ord(S[i])]+=1
    max_dis =0
    for i in range(256):
        if(c[i]!=0):
            max_dis+=1
    return max_dis
        




def find(S):
    n = len(S)
    max_dis = max_distinct(S,n)
    minimum_substring = n
    for i in range(n):
        for j in range(n):
            sub= S[i:j]
            sub_length = len(sub)
            sub_dis_char = max_distinct(sub,sub_length)
            if(sub_length<minimum_substring and max_dis==sub_dis_char):
                minimum_substring = sub_length
    return minimum_substring





    
S = input()
l = find(S);
print(l)
    
