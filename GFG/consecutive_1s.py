def count_1s(n):
    current=0
    max_so_far=0
    for i in range(len(n)):
        if n[i] == 1:
            current+=1
            max_so_far=max(max_so_far,current)
        else:
            current=0
    return max_so_far

l=list(map(int,input().split()))
print(count_1s(l))
