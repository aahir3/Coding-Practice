# cook your dish here
DECODER = 0b00000000000000001111111111111111
for T in range(int(input())):
    arr=[]
    a=[]
    b=[]
    for i in range(int(input())):
        arr.append(int(input()))
    l=len(arr)
    for i in range(l):
        b.append(arr[i]>>16)
        a.append(arr[i]&DECODER)
    print(f'Case {T+1}:')
    for i in range(l):
        print(a[i],end=" ")
    print()
    for i in range(l):    
        print(b[i],end=" ")